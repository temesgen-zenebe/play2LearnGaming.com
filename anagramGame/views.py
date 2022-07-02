from django.views.generic import TemplateView
# Create your views here.
class AnagramGameView(TemplateView):
    template_name = 'anagramGame/game.html'
class ScoreAnagramGameView(TemplateView):
    template_name = 'anagramGame/anagramScore.html'