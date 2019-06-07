# api/urls.py
from django.urls import include, path
from django.conf.urls import url
from api.views import *
from rest_framework.routers import DefaultRouter


# Schema parsing views

from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='ProjeX API Schema')


router = DefaultRouter(trailing_slash=False)
router.register(r'projects', ProjectViewSet)
router.register(r'memberships', UserProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'assignees', AssigneesViewSet)
router.register(r'preferences', PreferencesViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('schema/', schema_view),
]
