# Django
from django.urls import reverse

# Third Party
from authentication.models import Registration, User
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase


class TestObtainTokenApi(APITestCase):
    def create_user(self):
        url = reverse("authentication:users-list")
        data = {
            "first_name": "bahadir",
            "last_name": "kacar",
            "email": "bahadir@mail.com",
            "password": "AbCd123!!.:D",
        }
        self.client.post(url, data, format="json")
        return User.objects.get(email="bahadir@mail.com")

    def verify_user(self, user):
        registration = Registration.objects.get(user=user)
        verification_key = registration.verification_key
        url_verify = reverse(
            "authentication:registration-verify",
            kwargs={"verification_key": verification_key},
        )
        response = self.client.get(url_verify, {}, format="json")

    def test_obtaining_token_without_verification(self):
        """
        Ensure we can not get token of unverified user
        """
        user = self.create_user()
        url = reverse("authentication:api-token-auth")
        data = {
            "username": user.email,
            "password": "AbCd123!!.:D",
        }
        request = self.client.post(url, data, format="json")
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_obtaining_token_with_verification(self):
        """
        Ensure we can get token of verified user
        """
        user = self.create_user()
        self.verify_user(user)
        url = reverse("authentication:api-token-auth")
        data = {
            "username": user.email,
            "password": "AbCd123!!.:D",
        }
        request = self.client.post(url, data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
