from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import datetime

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


def project_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/project_<id>/<filename>
    return 'project_{0}/{1}'.format(instance.project.id, filename)

def tasks_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/task_<id>/<filename>
    return 'task_{0}/{1}'.format(instance.task.id, filename)


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, name, profile_photo, country, password=None):
        user = self.model(
            email=self.normalize_email(email),
            profile_photo = profile_photo,
            country = country,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, profile_photo, country, password):
        user = self.create_user(
            email,
            password=password,
            profile_photo = profile_photo,
            country = country,
            name=name,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, profile_photo, country, password):
        user = self.create_user(
            email,
            password=password,
            profile_photo = profile_photo,
            country = country,
            name= "True",
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# User(id, email, name, password, attachment_id, country_id)

# Note: A new implementation of user was required for Django REST Framework

class User(AbstractBaseUser):
    email = models.EmailField(max_length=70, unique=True)
    name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to=user_directory_path)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True,)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'name' ]

    def __str__(self):              # __unicode__ on Python 2
        return self.email


# Country(id, name)

class Country(models.Model):
    name = models.CharField(max_length = 30)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name


# Preferences (user_id, language, color_schema)

class Preferences(models.Model):
    language = models.CharField(max_length=2)
    color_schema = models.CharField(max_length=1)
    user = models.OneToOneField('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.language

# Project(id, title, description, attachment_id, creator_id)

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    project_photo = models.ImageField(upload_to=project_directory_path)
    creator = models.ForeignKey('User', on_delete=models.CASCADE, related_name="creator")
    asignees = models.ManyToManyField(
        'User',
        through='UserProject',
        through_fields=('project', 'user'),
        related_name="asignees"
    )

# Task(id, title, description, due_date, priority, attachment_id, project_id,, board_id)

class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    due_date = models.DateField(auto_now = False, auto_now_add = False )
    priority = models.IntegerField()
    task_file = models.FileField(upload_to=tasks_directory_path)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    asigned_users = models.ManyToManyField(
        'User',
        through='Asignees',
        through_fields=('task', 'user'),
        related_name="asigned_users"
    )

# Assignees(user_id, task_id)

class Asignees(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user")
    task = models.ForeignKey('Task', on_delete=models.CASCADE)

# Board(id, title)

class Board(models.Model):
    title = models.CharField(max_length=10)

# Comment(id, text, task_id, creator_id)

class Comment(models.Model):
    text = models.TextField()
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    creator = models.ForeignKey('User', on_delete=models.CASCADE)

# Notification(id, type, text, notifier_id)

class Notification(models.Model):
    notifier_type = models.CharField(max_length=10)
    notifier = models.IntegerField()
    receivers = models.ManyToManyField(
        'User',
        through='UserNotification',
        through_fields=('notification', 'user')
    )

# UserProject(user_id, project_id, status, role)

class UserProject(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.role

# UserNotification(user_id, notification_id)

class UserNotification(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    notification = models.ForeignKey('Notification', on_delete=models.CASCADE)


