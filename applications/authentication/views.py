# Third Party
from rest_framework import mixins, permissions, viewsets

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response

# Local Folder
from .models import Registration, User
from .serializers import (
    RegistrationSerializer,
    UserSerializer,
)

__all__ = [
    "UserViewset",
    "RegistrationViewSet",
]


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, validated_data):
        obj = OriginalModel.objects.create(**validated_data)
        obj.save(foo=validated_data["foo"])
        return obj
