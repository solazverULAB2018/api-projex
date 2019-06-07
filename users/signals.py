from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from api.models import Preferences, UserProject, Notification, UserNotification
from asgiref.sync import async_to_sync

######################################
############# TO DO ##################

# 1.- Invitation notification
# 2.- Assignment notification
# 3.- Comment notification
# 4.- Finish notification

@receiver(post_save, sender=CustomUser)
def create_user_preferences(sender, instance, created, **kwargs):

    if created:
        Preferences.objects.create(user=instance, color_schema='0', language="en")

@receiver(post_save, sender=CustomUser)
def save_user_preferences(sender, instance, **kwargs):
    instance.preferences.save()

@receiver(post_save, sender=UserProject)
def send_invitations(sender, instance, created, **kwargs):

    if created:
        notification = Notification.objects.create(notifier_type="project", notifier=instance.id)
        user = instance.user
        invitation = UserNotification.objects.create(user=user, notification=notification)