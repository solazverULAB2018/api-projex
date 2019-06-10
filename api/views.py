from rest_framework import viewsets, permissions
from api.models import *
from api.serializers import *

class UserProjectViewSet(viewsets.ModelViewSet):
    """
    API UserProjects memberships views
    """
    queryset = UserProject.objects.all()
    serializer_class = UserProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return UserProject.objects.filter(user=user)

class AssigneeViewSet(viewsets.ModelViewSet):
    """
    API Assignee views
    """
    queryset = Assignee.objects.all()
    serializer_class = AssigneeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        task_id = self.request.query_params.get('task')
        task = Task.objects.get(pk=task_id)
        return Assignee.objects.filter(task=task)

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API Projects views using DRF Viewsets
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        projects = Project.objects.filter(creator=user)
        memberships = UserProject.objects.filter(user=user)
        for instance in memberships:
            project = instance.get('project')
            projects.append(Project.objects.get(pk=project.id))
        return projects

class TaskViewSet(viewsets.ModelViewSet):
    """
    API Tasks views using DRF Viewsets
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        board_id = self.request.query_params.get('board')
        board = Board.objects.get(pk=board_id)
        return Task.objects.filter(board=board)

class CommentViewSet(viewsets.ModelViewSet):
    """
    API Comment views using DRF Viewsets
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

class BoardViewSet(viewsets.ModelViewSet):
    """
    API Board views using DRF Viewsets
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticated,)

class PreferencesViewSet(viewsets.ModelViewSet):
    """
    API Preferences views using DRF Viewsets
    """
    queryset = Preferences.objects.all()
    serializer_class = PreferencesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Preferences.objects.get(pk=user)

class NotificationViewSet(viewsets.ModelViewSet):
    """
    API Preferences views using DRF Viewsets
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        notifications = []
        user_notifications = UserNotification.objects(user=user)
        for notif in user_notifications:
            notifications.append(Notification.objects.get(pk=notif.notification))