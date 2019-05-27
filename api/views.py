from rest_framework import viewsets, permissions
from api.models import Project, UserProject
from api.serializers import ProjectSerializer, UserProjectSerializer

class UserProjectViewSet(viewsets.ModelViewSet):
    """
    API UserProjects memberships views
    """
    queryset = UserProject.objects.all()
    serializer_class = UserProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API Projects views using DRF Viewsets
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
