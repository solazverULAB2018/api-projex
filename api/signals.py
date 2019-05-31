from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from api.models import Project, Board


@receiver(post_save, sender=Project)
def create_project_board(sender, instance, created, **kwargs):

    if created:
        Board.objects.create(project=instance, title="todo")
        Board.objects.create(project=instance, title="doing")
        Board.objects.create(project=instance, title="done")

@receiver(post_save, sender=Project)
def save_project_board(sender, instance, **kwargs):
    instance.preferences.save()