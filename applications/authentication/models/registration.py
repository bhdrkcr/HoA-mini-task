# Standard Library
import uuid

# Django
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

__all__ = ["Registration"]


def create_verification_key():
    """creates a unique identifier for user mail verification"""
    return uuid.uuid4()


class Registration(models.Model):
    created_at = models.DateTimeField(
        _("created at"), auto_now=False, auto_now_add=True
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=_("Registred user"),
        on_delete=models.CASCADE,
        related_name="registrations",
    )
    verification_key = models.CharField(
        _("verification key"),
        default=create_verification_key,
        max_length=36,
        unique=True,
    )

    def send_registration_mail(self):
        current_site = Site.objects.get_current()

        send_mail(
            _("Verification for email from House of Apps"),
            _("click here to verify: ")
            + current_site.domain
            + reverse(
                "authentication:registration-verify",
                kwargs={"verification_key": self.verification_key},
            ),
            "app@gmail.com",
            [self.user.email],
            fail_silently=False,
        )
