from dataclasses import field
from django.forms import ModelForm
from .models import Games_comment,Contact



class GameCommentForm(ModelForm):
    class Meta:
        model = Games_comment
        fields = ('email', 'comment')
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name','email','subject','message')
