from django.urls import path
from .views import *
from .views import(
    ScoreMathList,
    MathGameView,
    ScoreMathGameView,
    MathGameDetailView,
    ScoreMathCreateView,
    MathScoreUserView,
    AllScoreMathList,
)
from math_game.views import ScoreMathForm

  
app_name = 'math_game' 

urlpatterns = [
    path('math-game-main', ScoreMathList.as_view(), name="score-math-list"),
    path('math-game-main', MathGameView.as_view(), name='math-game-main'),
    path('score-math/', MathScoreUserView.as_view(), name='score-math'),
    #path('math-game-main/<int:pk>/', MathGameDetailView.as_view(), name='detail'),
    path('math-score', AllScoreMathList.as_view(), name='all-math-score'),
    path('math-score', ScoreMathGameView.as_view(), name='math-score'),
    #path('math-game-main/create/', ScoreMathCreateView.as_view(),name='create'),
    path('',ScoreMathForm, name ='scoreMathForm'),
]