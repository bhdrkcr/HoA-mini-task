"""api_of_mugs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Third Party
from rest_framework.routers import DefaultRouter

# Local Folder
from .views import (
    ObtainAuthTokenWithVerificationCheck,
    RegistrationRetrieveAPIView,
    UserDetailRetrieveAPIView,
    UserViewset,
)

app_name = "authentication"

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"users", UserViewset, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "registrations/<uuid:verification_key>/verify",
        RegistrationRetrieveAPIView.as_view(),
        name="registration-verify",
    ),
    path(
        "profile/",
        UserDetailRetrieveAPIView.as_view(),
        name="profile",
    ),
    path(
        "api-token-auth/",
        ObtainAuthTokenWithVerificationCheck.as_view(),
        name="api-token-auth",
    ),
]
