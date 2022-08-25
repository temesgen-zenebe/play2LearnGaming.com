
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import LoggedUser
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
    
@admin.register(LoggedUser)
class LoggedUserAdmin(admin.ModelAdmin):
    model = LoggedUser
    list_display = ('id' ,'users',)
    list_filter = ('id' ,'users',)
    search_fields = ('users',)




