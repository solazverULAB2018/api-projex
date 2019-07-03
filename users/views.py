# users/views.py
from rest_framework import viewsets
from users.models import *
from . import models
from . import serializers
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=False, methods=['GET'], name='Get Current User')
    def current_user(self, params):
        user = serializers.UserSerializer(self.request.user)
        return Response(user.data)
