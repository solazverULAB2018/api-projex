from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from users.models import CustomUser
from api.models import Preferences

@receiver(post_save, sender=CustomUser)
def create_user_preferences(sender, instance, created, **kwargs):

    if created:
        Preferences.objects.create(user=instance, color_schema='0', language="en")

@receiver(post_save, sender=CustomUser)
def save_user_preferences(sender, instance, **kwargs):
    instance.preferences.save()