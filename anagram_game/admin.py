from django.contrib import admin
from .models import Anagram_score


# Register your models here.
@admin.register(Anagram_score)
class AnagrameScoreAdmin(admin.ModelAdmin):
    model = Anagram_score
    list_display = ['id', 'word_size', 'score', 'point','created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('score','created')
        return ()