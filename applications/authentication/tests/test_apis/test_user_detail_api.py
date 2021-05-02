# Django
from django.urls import reverse

# Third Party
from authentication.models import Registration, User
from model_bakery import baker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, RequestsClient


class TestUserDetailApi(APITestCase):
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

    def test_detail_without_verification(self):
        """
        Ensure we can not get detail of unverified user
        """
        user = self.create_user()
        url = reverse("authentication:profile")
        self.assertEqual(Token.objects.all().count(), 0)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + "")
        request = self.client.get(
            url,
            None,
        )
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_detail_with_verification(self):
        """
        Ensure we can get detail of verified user
        """

        user = self.create_user()
        self.verify_user(user)
        url = reverse("authentication:profile")
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        request = self.client.get(
            url,
            None,
            **{"Authorization": " Token " + token.key},
        )
        self.assertEqual(request.status_code, status.HTTP_200_OK)
