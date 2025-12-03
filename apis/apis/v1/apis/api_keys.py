from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apis.apis.v1.serializers.api_keys import APIKeyReadSerializer
from apis.base_api import BaseAPI
from apis.exceptions import APIException
from apis.methods import create_api_key


class APIKeysAPI(BaseAPI):
    permission_classes = [AllowAny]

    def create(self, request):
        username, password = request.data.get("username"), request.data.get("password")
        user = authenticate(username=username, password=password)

        if not user:
            raise APIException(
                message="Invalid credentials", code="invalid_credentials"
            )

        api_key = create_api_key(user)
        serializer = APIKeyReadSerializer(instance=api_key)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
