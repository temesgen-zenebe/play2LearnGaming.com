from dataclasses import field
from django.forms import ModelForm
from .models import Math_score,Comment_math

class MathScoreForm(ModelForm):
    class Meta:
        model = Math_score
        fields = ('operator' ,'max_range' ,'score', 'point')

class CommentForm(ModelForm):
    class Meta:
        model = Comment_math
        fields = ('game_type', 'comment')