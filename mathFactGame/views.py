from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class MathFactGameView(TemplateView):
    template_name = 'mathFactGame/game.html'
    
class ScoreMathFactGameView(TemplateView):
    template_name = 'mathFactGame/mathScore.html'