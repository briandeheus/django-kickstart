from django.conf import settings
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from apis.methods import create_api_key


User = get_user_model()


class BaseV1APITestCase(APITestCase):
    """Base test case for V1 API tests with common setup methods"""

    def setUp(self):
        """Set up test data before each test"""
        self.client = APIClient()
        self.user = self.create_user()
        self.api_key = create_api_key(self.user)

    def create_user(
        self, username="testuser", email="test@example.com", password="testpass123"
    ):
        """Create a test user"""
        return User.objects.create_user(
            username=username, email=email, password=password
        )

    def get_auth_headers(self, api_key=None):
        """Get authentication headers with Bearer token"""
        if api_key is None:
            api_key = self.api_key
        return {"HTTP_AUTHORIZATION": f"{settings.API_AUTH_SCHEME} {api_key.key}"}
