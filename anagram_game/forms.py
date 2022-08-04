from dataclasses import field
from django.forms import ModelForm
from .models import Anagram_score

class AnagrameScoreForm(ModelForm):
    class Meta:
        model = Anagram_score
        fields = ('word_size' ,'score', 'point')