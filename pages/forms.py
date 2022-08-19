from dataclasses import field
from django.forms import ModelForm
from .models import Games_comment



class GameCommentForm(ModelForm):
    class Meta:
        model = Games_comment
        fields = ('email', 'comment')