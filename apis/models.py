from django.db import models


class APIKey(models.Model):
    description = models.CharField(max_length=100, null=True, blank=True)
    key = models.CharField(max_length=100)
    user = models.ForeignKey(
        "core.CoreUser", related_name="api_keys", on_delete=models.CASCADE
    )
