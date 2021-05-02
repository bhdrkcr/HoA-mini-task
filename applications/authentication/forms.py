# Django
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

# Third Party
from captcha.fields import ReCaptchaField

__all__ = [
    "CustomLoginForm",
]


class CustomLoginForm(AuthenticationForm):
    captcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
    )

    error_messages = {
        **AuthenticationForm.error_messages,
        "invalid_login": _(
            "Please enter the correct %(username)s and password for a staff "
            "account. Note that both fields may be case-sensitive."
        ),
    }
    required_css_class = "required"

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_staff:
            raise self.ValidationError(
                self.error_messages["invalid_login"],
                code="invalid_login",
                params={"username": self.username_field.verbose_name},
            )
