from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137112ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137112", Testconnectors137112ViewSet, basename="testconnectors137112"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
