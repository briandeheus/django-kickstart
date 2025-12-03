from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apis.apis.v1.serializers.accounts import AccountsReadSerializer
from apis.apis.v1.serializers.api_keys import APIKeyReadSerializer
from apis.base_api import BaseAPI
from apis.exceptions import APIException, APINotFound
from apis.methods import create_api_key


class AccountsAPI(BaseAPI):
    permission_classes = [IsAuthenticated]
    SELF_NAME = "me"

    def retrieve(self, request, id):
        if id != self.SELF_NAME:
            raise APINotFound(code="not_found")

        account = AccountsReadSerializer(instance=request.user)
        return Response(account.data, status=status.HTTP_200_OK)
