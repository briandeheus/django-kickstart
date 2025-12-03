import logging
import secrets
import string
from typing import Tuple

from django.conf import settings
from apis.models import APIKey
from core.models import CoreUser

log = logging.getLogger(__name__)


def generate_secure_string(n=32):
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(n))


def create_api_key(user: CoreUser):
    key = (
        f"{settings.API_KEY_PREFIX}-{generate_secure_string(n=settings.API_KEY_LENGTH)}"
    )
    return APIKey.objects.create(user=user, key=key)


def get_user_from_api_key(
    auth_header: str = None,
) -> Tuple[CoreUser, APIKey] | Tuple[None, None]:
    if not auth_header or not auth_header.startswith(f"{settings.API_AUTH_SCHEME} "):
        return None, None

    auth_header = auth_header.split(" ")

    if len(auth_header) != 2:
        return None, None
    api_key = auth_header[1]

    try:
        api_key = APIKey.objects.prefetch_related("user").get(key=api_key)
        user = api_key.user
        log.debug("Found user=%s locally from API key", user.pk)
        return user, api_key
    except APIKey.DoesNotExist:
        log.debug("API key not found locally")
        return None, None
