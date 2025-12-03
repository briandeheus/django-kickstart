from django.urls import path, include

urlpatterns = [
    path("v1/", include("apis.apis.v1.router"), name="v1_router"),
]
