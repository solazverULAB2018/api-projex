# users/urls.py
from django.urls import include, path
from .views import UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]