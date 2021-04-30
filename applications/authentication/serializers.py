# Third Party
from rest_framework import serializers

# Local Folder
# Local Folderry
from .models import Registration, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]


class RegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    verification_key = serializers.ReadOnlyField()

    class Meta:
        model = Registration
        exclude = []
