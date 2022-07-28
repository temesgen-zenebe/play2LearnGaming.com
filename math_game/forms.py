from dataclasses import field
from django.forms import ModelForm
from .models import Math_score

class MathScoreForm(ModelForm):
    class Meta:
        model = Math_score
        fields = ('operator' ,'max_range' ,'score', 'point')