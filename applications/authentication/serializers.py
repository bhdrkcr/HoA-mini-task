# Standard Library
import sys

# Django
import django.contrib.auth.password_validation as validators
from django.core import exceptions

# Third Party
from rest_framework import serializers

# Local Folder
# Local Folderry
from .models import Registration, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Registration.objects.create(user=user)
        return user

    def validate(self, data):
        # here data has all the fields which have validated values
        # so we can create a User instance out of it
        user = User(**data)

        # get the password from the data
        password = data.get("password")

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=User)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors["password"] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSerializer, self).validate(data)


class RegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    verification_key = serializers.ReadOnlyField()

    class Meta:
        model = Registration
        lookup_field = "verification_key"
        exclude = []
