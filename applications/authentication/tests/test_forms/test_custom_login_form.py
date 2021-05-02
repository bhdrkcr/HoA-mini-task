# Standard Library
from unittest.mock import MagicMock, PropertyMock, patch

# Django
from django.test import TestCase  # Django
from django.urls import reverse

# Third Party
from authentication.forms import CustomLoginForm
from authentication.models import User
from captcha.client import RecaptchaResponse


class TestCustomLoginForm(TestCase):
    def setUp(self):
        self.password = "Test123++1"
        self.user = User.objects.create_superuser(
            email="user@mail.com", password=self.password
        )

    @patch("captcha.fields.client.submit")
    def test_login_with_captcha_passed(self, mocked_submit):
        mocked_submit.return_value = RecaptchaResponse(is_valid=True)
        # send login data to form directly
        form = CustomLoginForm(
            data={
                "username": self.user.email,
                "password": self.password,
                "g-recaptcha-response": "PASSED",
            }
        )
        self.assertTrue(form.is_valid())

    @patch("captcha.fields.client.submit")
    def test_login_without_captcha_passed(self, mocked_submit):
        mocked_submit.return_value = RecaptchaResponse(is_valid=False)
        # send login data to form directly
        form = CustomLoginForm(
            data={
                "username": self.user.email,
                "password": self.password,
                "g-recaptcha-response": "FAIL",
            }
        )
        self.assertFalse(form.is_valid())

    @patch("captcha.fields.client.submit")
    def test_login_without_staff_user(self, mocked_submit):
        mocked_submit.return_value = RecaptchaResponse(is_valid=True)
        # send login data to form directly
        self.user.is_staff = False
        self.user.save()
        form = CustomLoginForm(
            data={
                "username": self.user.email,
                "password": self.password,
                "g-recaptcha-response": "PASSED",
            }
        )
        self.assertFalse(form.is_valid())
