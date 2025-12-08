from rest_framework import status

from apis.apis.v1.tests.base import BaseV1APITestCase


class TestAuthentication(BaseV1APITestCase):
    def test_retrieve_account_authenticated(self):
        """Test retrieving account info with valid authentication"""
        response = self.client.get("/api/v1/accounts/me/", **self.get_auth_headers())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")
        self.assertEqual(response.data["email"], "test@example.com")

    def test_retrieve_account_unauthenticated(self):
        """Test retrieving account info without authentication"""
        response = self.client.get("/api/v1/accounts/me/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_account_invalid_api_key(self):
        """Test retrieving account info with invalid API key"""
        response = self.client.get(
            "/api/v1/accounts/me/", HTTP_AUTHORIZATION="Bearer invalid-key-123"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_account_non_me_endpoint(self):
        """Test that only 'me' endpoint is allowed"""
        response = self.client.get("/api/v1/accounts/123/", **self.get_auth_headers())
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
