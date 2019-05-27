from rest_framework import serializers
from users.models import CustomUser
from api.models import Project, Task, UserProject
from users.serializers import UserSerializer
import pdb


class UserProjectSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all())
    project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(), required=False)

    class Meta:
        model = UserProject
        fields = ('id','user', 'project', 'role', 'status')


class ProjectSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all())
    project_to_user = UserProjectSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description',
                  'project_photo', 'creator', 'project_to_user')

    def create(self, validated_data):
        users_data = validated_data.pop('project_to_user')
        project = Project.objects.create(**validated_data)
        for data in users_data:
            UserProject.objects.create(project=project, **data)
        return project

    ######## TODO UPDATE USING PROJECT VIEW ##############


    # def update(self, instance, validated_data):
    #     users_data = validated_data.pop('project_to_user')
    #     assignees_data = UserProject.objects.get(project=instance)
    #     instance.update(**validated_data)
    #     for data in assignees_data:
    #         data.create_or_update(**users_data)
            

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'due_date',
                  'priority', 'task_file', 'project', 'board')
