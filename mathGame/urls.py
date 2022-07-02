from django.urls import path

from .views import MathGameView,ScoreMathGameView

app_name = 'mathGame'
urlpatterns = [
    path('math-game', MathGameView.as_view(), name='math-game'),
    path('math-score', ScoreMathGameView.as_view(), name='math-score'),
]