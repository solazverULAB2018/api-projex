# api/urls.py
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, ObtainJSONWebToken
from rest_framework_jwt.views import refresh_jwt_token
from users.serializers import CustomJWTSerializer
import notifications.urls


urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    path('api-token-refresh/', refresh_jwt_token),
    path('^inbox/notifications/', include(notifications.urls, namespace='notifications')),

]