from dataclasses import field
from django.forms import ModelForm
from .models import Anagram_score,Comment_Anagram

class AnagrameScoreForm(ModelForm):
    class Meta:
        model = Anagram_score
        fields = ('users','word_size' ,'score', 'point')
        
class CommentAnagrameForm(ModelForm):
    class Meta:
        model = Comment_Anagram
        fields = ('game_type', 'comment')