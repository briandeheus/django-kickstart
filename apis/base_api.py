import logging
import time
import traceback

from django.db.models import ObjectDoesNotExist
from rest_framework import response, viewsets, status

from apis.authentication import APIKeyAuthentication
from apis.exceptions import APIAccessDenied, APIException, APINotFound

log = logging.getLogger(__name__)


class BaseAPI(viewsets.GenericViewSet):
    authentication_classes = [APIKeyAuthentication]
    lookup_field = "id"

    def __init__(self, **kwargs):
        self.start_time = time.time()
        super().__init__(**kwargs)

    def get_runtime(self) -> float:
        return time.time() - self.start_time

    def finalize_response(self, request, response, *args, **kwargs):
        end_time = self.get_runtime()
        logging.debug(
            "API call api=%s method=%s path=%s elapsed=%s",
            self.get_view_name(),
            self.request.method,
            self.request.path,
            end_time,
        )
        return super().finalize_response(request, response, *args, **kwargs)

    def handle_exception(self, exc):
        try:
            return super().handle_exception(exc)
        except ObjectDoesNotExist:
            return response.Response(
                {"error": "Object not found", "code": "not_found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except APINotFound as e:
            return response.Response(
                {"error": e.message, "code": e.code}, status=status.HTTP_404_NOT_FOUND
            )
        except APIAccessDenied as e:
            return response.Response(
                {"error": e.message, "code": e.code},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except APIException as e:
            return response.Response(
                {"error": e.message, "code": e.code}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception:
            tb = traceback.TracebackException.from_exception(exc)
            logging.error(
                "Uncaught exception in api=%s method=%s user=%s path=%s\n\n%s\n%s",
                "".join(tb.format()),
                self.get_view_name(),
                self.request.method,
                self.request.user,
                self.request.path,
                exc,
                tb,
            )
            return response.Response(
                {"error": "Something went wrong.", "code": "unknown"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
