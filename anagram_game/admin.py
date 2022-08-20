from django.contrib import admin
from .models import Anagram_score,Comment_Anagram


# Register your models here.
@admin.register(Anagram_score)
class AnagrameScoreAdmin(admin.ModelAdmin):
    model = Anagram_score
    list_display = ['id', 'users', 'word_size', 'score', 'point','created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('score','created')
        return ()
    
# Register your models here.
@admin.register(Comment_Anagram)
class CommentAnagramGame(admin.ModelAdmin):
    list_display = ('user', 'game_type','comment', 'created','active',)
    list_filter = ('active', 'created')
    search_fields = ('user', 'created')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)