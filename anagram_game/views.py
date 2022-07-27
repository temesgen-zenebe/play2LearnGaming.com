from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AnagramView(TemplateView):
    template_name = 'anagram_game/anagram_main.html'
    
class ScoreAnagramView(TemplateView):
    template_name = 'anagram_game/anagram_score.html'