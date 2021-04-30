# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Local Folder
from .models import User

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "is_staff", "is_active"]
    list_filter = ("email", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("General", {"fields": ("first_name", "last_name", "avatar", "groups")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
        ("General", {"fields": ("first_name", "last_name", "avatar", "groups")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    ordering = ("email",)
