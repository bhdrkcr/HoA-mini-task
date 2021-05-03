# Django
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import AdminSite
from django.test import Client, TestCase

# Third Party
from authentication.admin import (
    UnverifiedUserProxy,
    Users,
    VerifiedUserProxy,
    VerifiedUsers,
)
from authentication.forms import CustomLoginForm
from authentication.models import User


class TestAdmin(TestCase):
    def create_user(self):
        self.email = "test_admin@mail.com"
        self.password = User.objects.make_random_password()
        user, created = User.objects.get_or_create(email=self.email)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user_is_verified = True
        user.save()
        self.user = user

    def test_spider_admin(self):
        self.create_user()
        self.client.login(username=self.email, password=self.password)
        admin_pages = [
            "/admin/",
            # put all the admin pages for your models in here.
            "/admin/password_change/",
            "/admin/authentication/unverifieduserproxy/",
            "/admin/authentication/verifieduserproxy/",
        ]
        for page in admin_pages:
            request = self.client.get(page, {}, format="html")
            self.assertEqual(request.status_code, 200)
