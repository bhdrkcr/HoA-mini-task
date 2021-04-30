# Standard Library
import uuid

# Django
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = ["Registration"]


MAXIMUM_VALID_DAYS = 3


def create_verification_key(self):
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
