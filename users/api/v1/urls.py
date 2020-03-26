from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PhoneViewSet

router = DefaultRouter()
router.register("phone", PhoneViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
