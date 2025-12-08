from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CoreUser


@admin.register(CoreUser)
class CoreUserAdmin(UserAdmin):
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    search_fields = ["username", "email", "first_name", "last_name"]
    list_filter = ["is_staff", "is_superuser", "is_active", "groups"]
