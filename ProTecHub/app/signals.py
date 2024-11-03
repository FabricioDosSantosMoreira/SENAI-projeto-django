from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups(sender, **kwargs) -> None:
    if sender.name == 'app': 
        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='Supervisor')
        Group.objects.get_or_create(name='Colaborador')
