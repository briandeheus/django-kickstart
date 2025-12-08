from django.conf import settings
from rest_framework import status

from apis.apis.v1.tests.base import BaseV1APITestCase
from apis.models import APIKey


class TestApiKeys(BaseV1APITestCase):
    def test_create_api_key_success(self):
        """Test creating an API key with valid credentials"""
        response = self.client.post(
            "/api/v1/api-keys/",
            {"username": "testuser", "password": "testpass123"},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("key", response.data)
        self.assertTrue(response.data["key"].startswith(settings.API_KEY_PREFIX))

    def test_create_api_key_invalid_credentials(self):
        """Test creating an API key with invalid credentials"""
        response = self.client.post(
            "/api/v1/api-keys/",
            {"username": "testuser", "password": "wrongpassword"},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["code"], "invalid_credentials")

    def test_create_api_key_missing_credentials(self):
        """Test creating an API key with missing credentials"""
        response = self.client.post("/api/v1/api-keys/", {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_api_key_creates_database_record(self):
        """Test that creating an API key saves it to the database"""
        initial_count = APIKey.objects.count()
        response = self.client.post(
            "/api/v1/api-keys/",
            {"username": "testuser", "password": "testpass123"},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(APIKey.objects.count(), initial_count + 1)
