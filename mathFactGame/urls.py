from django.urls import path

from .views import MathFactGameView,ScoreMathFactGameView

app_name = 'mathFactGame'
urlpatterns = [
    path('math-fact-game', MathFactGameView.as_view(), name='math-fact-game'),
    path('math-fact-score', ScoreMathFactGameView.as_view(), name='math-fact-score'),
]