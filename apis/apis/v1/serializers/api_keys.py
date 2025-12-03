from rest_framework.serializers import ModelSerializer


from apis.models import APIKey


class APIKeyReadSerializer(ModelSerializer):
    class Meta:
        model = APIKey
        fields = ["key"]
