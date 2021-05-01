# Django
from django.test import TestCase

# Third Party
from authentication.models import User
from model_bakery import baker

# Create your tests here.


class TestUserModel(TestCase):
    def test_user_creation_baker(self):
        user = baker.make(User)
        self.assertTrue(isinstance(user, User))
        self.assertEqual(str(user), user.email)

    def test_create_superuser(self):
        rand = baker.make(User)
        user = User.objects.create_superuser(
            email="uniquemail0@m.com", password=rand.password
        )
        self.assertTrue(isinstance(user, User))
        self.assertTrue(User.is_superuser)
        self.assertEqual(str(user), user.email)

    def test_create_user(self):
        rand = baker.make(User)
        user = User.objects.create_user(
            email="uniquemail1@m.com", password=rand.password
        )
        self.assertTrue(isinstance(user, User))
        self.assertTrue(User.is_staff)
        self.assertEqual(str(user), user.email)

    def test_create_user_without_email(self):
        rand = baker.make(User)
        self.assertRaises(
            ValueError, User.objects.create_user, email="", password=rand.password
        )

    def test_create_superuser_without_staff(self):
        rand = baker.make(User)
        self.assertRaises(
            ValueError,
            User.objects.create_superuser,
            email="uniquemail2@m.com",
            password=rand.password,
            is_staff=False,
        )

    def test_create_superuser_without_super(self):
        rand = baker.make(User)
        self.assertRaises(
            ValueError,
            User.objects.create_superuser,
            email="uniquemail2@m.com",
            password=rand.password,
            is_superuser=False,
        )
