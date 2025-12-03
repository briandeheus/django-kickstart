from typing import Union, List, Tuple

from rest_framework.authentication import BaseAuthentication

from apis.models import APIKey
from apis.methods import get_user_from_api_key
from core.models import CoreUser


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request) -> Tuple[CoreUser, APIKey] | Tuple[None, None]:
        if not request.META.get("HTTP_AUTHORIZATION"):
            return None, None

        return get_user_from_api_key(auth_header=request.META.get("HTTP_AUTHORIZATION"))
