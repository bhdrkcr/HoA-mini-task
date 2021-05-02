# # Standard Library
# from unittest.mock import MagicMock, PropertyMock, patch

# # Django
# from django.contrib.auth.models import User
# from django.test import TestCase  # Django
# from django.urls import reverse


# class TestCustomLoginForm(TestCase):
#     def setUp(self):
#         self.credentials = {"username": "testuser", "password": "ABC123secret"}
#         self.login_url = "/admin/login"
#         User.objects.create_user(**self.credentials)

#     def test_login(self):
#         # send login data
#         response = self.client.post("/login/", self.credentials, follow=True)
#         # should be logged in now
#         self.assertTrue(response.context["user"].is_active)
#         read_mock = MagicMock()
#         read_mock.read.return_value = (
#             b'{"success": true, "challenge_ts":'
#             b'"2019-01-11T13:57:23Z", "hostname": "testkey.google.com"}'
#         )
#         mocked_response.return_value = read_mock
#         uuid_hex = uuid.uuid4().hex
#         response = client.submit(
#             uuid_hex,
#             "somekey",
#             "0.0.0.0",
#         )

#         # Quick way to test method call without needing to worry about Python 2
#         # dicts not being ordered by default.
#         self.assertIn("secret=somekey", mocked_response.call_args.__str__())
#         self.assertIn("response=%s" % uuid_hex, mocked_response.call_args.__str__())
#         self.assertIn("remoteip=0.0.0.0", mocked_response.call_args.__str__())
#         self.assertTrue(response.is_valid)
