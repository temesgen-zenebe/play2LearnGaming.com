
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import LoggedUser

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Optional Fields', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )
    
@admin.register(LoggedUser)
class LoggedUserAdmin(admin.ModelAdmin):
    model = LoggedUser
    list_display = ('id' ,'users',)
    list_filter = ('id' ,'users',)
    search_fields = ('users',)
