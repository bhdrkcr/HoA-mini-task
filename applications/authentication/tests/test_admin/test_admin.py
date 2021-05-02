# # Django
# from django.contrib.admin.options import ModelAdmin
# from django.contrib.admin.sites import AdminSite
# from django.test import TestCase

# # Third Party
# from authentication.admin import (
#     UnverifiedUserProxy,
#     Users,
#     VerifiedUserProxy,
#     VerifiedUsers,
# )
# from authentication.forms import CustomLoginForm
# from authentication.models import User


# class MockRequest:
#     pass


# class MockSuperUser:
#     def has_perm(self, perm, obj=None):
#         return True


# request = MockRequest()
# request.user = MockSuperUser()


# class TestAdmin(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user_verified = User.objects.create(
#             email="u@v.u", first_name="t", last_name="0", is_verified=True
#         )
#         cls.user_unverified = User.objects.create(
#             email="v@v.u", first_name="T", last_name="1", is_verified=True
#         )

#     def setUp(self):
#         self.site = AdminSite()

#     def test_modeladmin_str(self):
#         ma = ModelAdmin(VerifiedUsers, VerifiedUserProxy, self.site)
#         self.assertEqual(str(ma), "modeladmin.ModelAdmin")
