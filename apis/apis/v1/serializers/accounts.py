from rest_framework.serializers import ModelSerializer

from apis.models import APIKey
from core.models import CoreUser


class AccountsReadSerializer(ModelSerializer):
    class Meta:
        model = CoreUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
        ]
