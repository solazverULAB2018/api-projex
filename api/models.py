from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime
from users.models import CustomUser, AutoDateTimeField
from django.utils import timezone

# Create your models here.


def project_directory_path(instance, filename):
    # file will be uploaded to MEDIA_URL/project_<id>/
    return 'project_{0}/{1}'.format(instance.id, filename)


def tasks_directory_path(instance, filename):
    # file will be uploaded to MEDIA_URL/task_<id>/
    return 'task_{0}/{1}'.format(instance.id, filename)

# Preferences (user_id, language, color_schema)


class Preferences(models.Model):
    language = models.CharField(max_length=2)
    color_schema = models.CharField(max_length=1)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    def __str__(self):
        return self.language

# Project(id, title, description, attachment_id, creator_id)


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    project_photo = models.ImageField(
        upload_to=project_directory_path, blank=True)
    creator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="project_creator")
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    assignee = models.ManyToManyField(
        CustomUser,
        through='UserProject'
    )

# Task(id, title, description, due_date, priority, attachment_id, board_id)


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    priority = models.IntegerField()
    task_file = models.FileField(upload_to=tasks_directory_path, blank=True)
    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    assigned_users = models.ManyToManyField(
        CustomUser,
        through='Assignee'
    )
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)


# Assignee(user_id,  task_id)


class Assignee(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_to_task")
    task = models.ForeignKey(
        'Task', on_delete=models.CASCADE, related_name="task_to_user")
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)


# Board(id, title, project_id)


class Board(models.Model):
    title = models.CharField(max_length=10)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

# Comment(id, text, task_id, creator_id)


class Comment(models.Model):
    text = models.TextField()
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)


# Notification(id, type, text, notifier_id)


class Notification(models.Model):
    notifier_type = models.CharField(max_length=30)
    notifier = models.IntegerField()
    receivers = models.ManyToManyField(
        CustomUser,
        through='UserNotification',
        through_fields=('notification', 'user')
    )
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

# UserProject(user_id, project_id, status, role)


class UserProject(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_to_project")
    project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, related_name="project_to_user")
    role = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)


# UserNotification(user_id, notification_id)


class UserNotification(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_to_notification")
    notification = models.ForeignKey(
        'Notification', on_delete=models.CASCADE, related_name="notification_to_user")
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
