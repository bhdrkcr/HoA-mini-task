# Django
from django.urls import reverse

# Third Party
from authentication.models import Registration, User
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase


class TestRegistrationApi(APITestCase):
    def test_register(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse("authentication:users-list")
        data = {
            "first_name": "bahadir",
            "last_name": "kacar",
            "email": "bahadir@mail.com",
            "password": "AbCd123!!.:D",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(
            User.objects.get().first_name,
            "bahadir",
            "created users name is name of given user",
        )

    def test_register_bad_password(self):
        """
        Ensure we can not create user with bad password
        """
        url = reverse("authentication:users-list")
        data = {
            "first_name": "bahadir",
            "last_name": "kacar",
            "email": "bahadir@mail.com",
            "password": "12345",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_email_conflict(self):
        """
        If you already registered you will get conflict
        """
        url = reverse("authentication:users-list")
        data = {
            "first_name": "bahadir",
            "last_name": "kacar",
            "email": "bahadir@mail.com",
            "password": "AbCd123!!.:D",
        }
        self.client.post(url, data, format="json")
        double_response = self.client.post(url, data, format="json")
        self.assertEqual(double_response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(User.objects.count(), 1)


class TestRegistrationRetrieveAPI(APITestCase):
    def test_registration_retrive(self):
        """
        Ensure we can verify users from sent email.
        Users are not verified until opening verification page via sent mail
        """
        url = reverse("authentication:users-list")
        user = baker.make(User)
        data = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": "unique@mail.com",
            "password": user.password,
        }
        self.client.post(url, data, format="json")
        registration = Registration.objects.get(user__email="unique@mail.com")
        verification_key = registration.verification_key
        self.assertIsNotNone(verification_key)
        url_verify = reverse(
            "authentication:registration-verify",
            kwargs={"verification_key": verification_key},
        )
        self.assertFalse(
            User.objects.get(email="unique@mail.com").is_verified,
            "user is not verified until opening verification page",
        )
        response = self.client.get(url_verify, {}, format="json")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            "verification page opens up correctly",
        )
        self.assertTrue(
            User.objects.get(email="unique@mail.com").is_verified,
            "user is verified after opening verification page",
        )
