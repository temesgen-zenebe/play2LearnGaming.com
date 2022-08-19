from django.contrib import admin
from .models import Games_comment
 
# Register your models here.
@admin.register(Games_comment)
class GamesComment(admin.ModelAdmin):
    list_display = ('user', 'email', 'comment', 'created','active',)
    list_filter = ('active', 'created')
    search_fields = ('user', 'email' 'created')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)