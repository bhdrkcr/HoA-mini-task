# Third Party
from rest_framework import (
    mixins,
    permissions,
    status,
    viewsets,
)

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

    def create(self, request, *args, **kwargs):
        if User.objects.filter(email=request.POST.get("email")).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        return super(UserViewset, self).create(request, *args, **kwargs)


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    lookup_field = "verification_key"

    @action(detail=True)
    def validation(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user.is_verified = True
        instance.user.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
