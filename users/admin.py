
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

CustomUsers = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUsers

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Optional Fields', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )
    





