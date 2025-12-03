from rest_framework.routers import DefaultRouter

from apis.apis.v1.apis import api_keys, accounts

router = DefaultRouter()

router.register(r"api-keys", api_keys.APIKeysAPI, basename="api-keys")
router.register(r"accounts", accounts.AccountsAPI, basename="accounts")

urlpatterns = router.urls
