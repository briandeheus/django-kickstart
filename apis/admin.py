from django.conf import settings
from django.contrib import admin

from .methods import generate_secure_string
from .models import APIKey


@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ["id", "description", "user", "key"]
    search_fields = ["description", "key", "user__username", "user__email"]
    list_filter = ["user"]
    autocomplete_fields = ["user"]
    readonly_fields = ["key"]

    def get_fields(self, request, obj=None):
        if obj:
            return ["description", "user", "key"]
        else:
            return ["description", "user"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.key = f"{settings.API_KEY_PREFIX}-{generate_secure_string(n=settings.API_KEY_LENGTH)}"
        super().save_model(request, obj, form, change)
