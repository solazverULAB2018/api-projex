# users/views.py
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)