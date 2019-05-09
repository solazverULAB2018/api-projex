# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

def user_directory_path(instance):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/'.format(instance.user.id)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    profile_photo = models.ImageField(upload_to=user_directory_path, blank=True)
    country = models.ForeignKey('api.Country', on_delete=models.SET_NULL, null=True,)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'email' ]

    def __str__(self):              # __unicode__ on Python 2
        return self.email