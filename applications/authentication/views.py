# Third Party
from rest_framework import (
    generics,
    mixins,
    permissions,
    status,
    viewsets,
)
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
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
    "RegistrationRetrieveAPIView",
    "UserDetailRetrieveAPIView",
    "ObtainAuthTokenWithVerificationCheck",
]


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        if User.objects.filter(email=request.POST.get("email")).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        return super(UserViewset, self).create(request, *args, **kwargs)


class UserDetailRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True)
    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(self.request.user).data)


class RegistrationRetrieveAPIView(generics.RetrieveAPIView):
    """verify saved registration object from uuid"""

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    lookup_field = "verification_key"

    @action(detail=True)
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user.is_verified = True
        instance.user.save()
        return super(RegistrationRetrieveAPIView, self).get(request, *args, **kwargs)


class ObtainAuthTokenWithVerificationCheck(ObtainAuthToken):
    """Check if the user is verified and return token if not unauthorized"""

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if user.is_verified:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
