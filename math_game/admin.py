from django.contrib import admin
from .models import Math_score

# Register your models here.
@admin.register(Math_score)
class MathScoreAdmin(admin.ModelAdmin):
    model = Math_score

    list_display = ['id','user' ,'operator', 'max_range', 'score', 'point','created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('score','created')

        return ()
