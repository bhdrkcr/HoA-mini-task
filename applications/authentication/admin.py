# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Local Folder
from .models import User


# Register your models here.
class VerifiedUserProxy(User):
    class Meta:
        proxy = True


class UnverifiedUserProxy(User):
    class Meta:
        proxy = True


class Users(UserAdmin):
    model = User
    list_display = ["email", "is_staff", "is_active"]
    list_filter = ("email", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_verified")}),
        ("General", {"fields": ("first_name", "last_name", "groups")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
        ("General", {"fields": ("first_name", "last_name", "groups")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    ordering = ("email",)


@admin.register(VerifiedUserProxy)
class VerifiedUsers(Users):
    def get_queryset(self, request):
        return self.model.objects.filter(is_verified=True)


@admin.register(UnverifiedUserProxy)
class UnverifiedUsers(Users):
    def get_queryset(self, request):
        return self.model.objects.filter(is_verified=False)
