from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from api.models import Board, Project, Comment, Assignee, Preferences, UserProject, Notification, UserNotification
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


######################################
############# TO DO ##################

# 1.- Invitation notification CHECK
# 2.- Assignment notification CHECK
# 3.- Comment notification
# 4.- Finish notification

def send_notification(user, content):
    group_name = 'user_%s' % user.id
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(group_name, content)


@receiver(post_save, sender=CustomUser)
def create_user_preferences(sender, instance, created, **kwargs):

    if created:
        Preferences.objects.create(
            user=instance, color_schema='0', language="en")


@receiver(post_save, sender=CustomUser)
def save_user_preferences(sender, instance, **kwargs):
    instance.preferences.save()


@receiver(post_save, sender=Project)
def create_project_board(sender, instance, created, **kwargs):

    if created:
        Board.objects.create(project=instance, title="todo")
        Board.objects.create(project=instance, title="doing")
        Board.objects.create(project=instance, title="done")


@receiver(post_save, sender=Project)
def save_project_board(sender, instance, **kwargs):
    boards_set = instance.board_set.all()

    for board in boards_set:
        board.save()


def create_notification(notifier_type, user, instance):
    notification = Notification.objects.create(
        notifier_type=notifier_type, notifier=instance.id)
    notification.save()
    invitation = UserNotification.objects.create(
        user=user, notification=notification)
    invitation.save()


def insert_content(payload):
    return {
        "type": "notify",
        "payload": payload
    }


@receiver(post_save, sender=UserProject)
def send_invitations(sender, instance, created, **kwargs):

    if created:
        user = instance.user
        create_notification("project", user, instance)
        payload = {
            "project": instance.project.id,
            "notifier_type": "project",
            "role": instance.role
        }
        content = insert_content(payload)
        # send_notification(user, content)


@receiver(post_save, sender=Assignee)
def send_assignations(sender, instance, created, **kwargs):

    if created:
        user = instance.user
        create_notification("assignation", user, instance)
        payload = {
            "project": instance.project.id,
            "notifier_type": "project",
            "role": instance.role
        }
        content = insert_content(payload)
        # send_notification(user, content)
