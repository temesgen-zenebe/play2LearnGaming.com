from django.views.generic import TemplateView
# Create your views here.
class MathGameView(TemplateView):
    template_name = 'mathGame/game.html'
class ScoreMathGameView(TemplateView):
    template_name: str = 'mathGame/mathScore.html'