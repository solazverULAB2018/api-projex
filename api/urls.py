# api/urls.py
from django.urls import include, path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, ObtainJSONWebToken
from rest_framework_jwt.views import refresh_jwt_token
from users.serializers import CustomJWTSerializer
import notifications.urls

from api.views import ProjectViewSet, UserProjectViewSet
from rest_framework.routers import DefaultRouter


# Schema parsing views

from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='ProjeX API Schema')


router = DefaultRouter(trailing_slash=False)
router.register(r'projects', ProjectViewSet)
router.register(r'memberships', UserProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/',
         ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    path('api-token-refresh/', refresh_jwt_token),
    path('schema/', schema_view),
    url('^inbox/notifications/',
        include(notifications.urls, namespace='notifications')),
]
