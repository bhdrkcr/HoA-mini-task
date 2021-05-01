# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthenticationConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "authentication"
    verbose_name = _("authentication")

    def ready(self):
        # Third Party
        import authentication.signals  # noqa
