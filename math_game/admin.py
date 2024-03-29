from django.contrib import admin
from .models import (
    Comment_math,
    Math_score,
    Addition_score,
    Multiplication_score,
    Division_score,
    Subtraction_score,
    
)
# Register your models here.
@admin.register(Math_score)
class MathScoreAdmin(admin.ModelAdmin):
    model = Math_score
    list_display = ['id','user' ,'operator', 'max_range', 'score', 'point','created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('score','created')

        return ()
        
# Register your models here.
@admin.register(Addition_score)
class AdditionScoreAdmin(admin.ModelAdmin):
    model = Addition_score
    list_display = ['id','user' ,'operator', 'max_range', 'score', 'point','created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','point','score','created',)

        return ()

@admin.register(Division_score)
class DivisionScoreAdmin(admin.ModelAdmin):
    model = Division_score
    list_display = ['id','user' ,'operator', 'max_range', 'score', 'point','created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','point','score','created',)

        return ()

@admin.register(Multiplication_score)
class MultiplicationScoreAdmin(admin.ModelAdmin):
    model = Multiplication_score
    list_display = ['id','user' ,'operator', 'max_range', 'score', 'point','created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','point','score','created',)

        return ()

@admin.register(Subtraction_score)
class SubtractionScoreAdmin(admin.ModelAdmin):
    model = Subtraction_score
    list_display = ['id','user' ,'operator', 'max_range', 'score', 'point','created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','point','score','created',)

        return ()

@admin.register(Comment_math)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created','game_type', 'active',)
    list_filter = ('active', 'created')
    search_fields = ('user', 'game_type', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)