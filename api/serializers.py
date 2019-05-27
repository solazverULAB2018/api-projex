from rest_framework import serializers
from users.models import CustomUser
from api.models import Project, Task
from users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    assignees = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())
    class Meta:
        model = Project
        fields = ('id','title', 'description',
                  'project_photo', 'creator', 'assignees')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'due_date',
                  'priority', 'task_file', 'project', 'board')
