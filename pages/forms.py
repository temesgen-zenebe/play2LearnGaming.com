from dataclasses import field
from tkinter import Widget
from django.forms import ModelForm,Textarea
from .models import Games_comment,Contact



class GameCommentForm(ModelForm):
    class Meta:
        model = Games_comment
        fields = ('email', 'comment')
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name','email','subject','message')
        widgets = {
            'message': Textarea(attrs={'cols': 30, 'rows': 4}),
        }
        labels = {
            'email': "Email",
        }