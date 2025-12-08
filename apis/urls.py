from django.urls import include, path

urlpatterns = [
    path("v1/", include("apis.apis.v1.router"), name="v1_router"),
]
