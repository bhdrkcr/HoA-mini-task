# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Local Folder
from .models import Registration, User


@receiver(post_save, sender=Registration)
def create_registration(sender, instance, created, **kwargs):
    if created:
        instance.send_registration_mail()
