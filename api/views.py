from rest_framework import viewsets
from api.models import Project
from api.serializers import ProjectSerializer
from rest_framework import permissions

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)