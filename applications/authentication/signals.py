# Django
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Third Party
from rest_framework.authtoken.models import Token

# Local Folder
from .models import Registration


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Registration.objects.create(user=instance)
    if instance.is_verified:
        Token.objects.get_or_create(user=instance)


@receiver(post_save, sender=Registration)
def create_registration(sender, instance, created, **kwargs):
    if created:
        instance.send_registration_mail()
