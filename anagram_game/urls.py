from django.urls import path
from .views import *
from .views import (
    AnagramGameView,
    AnagramGameDetailView,
    ScoreAnagramView,
    ScoreAnagramCreateView,
    ScoreAnagrameList,
)


app_name = 'anagram_game' 

urlpatterns = [
    path('anagram-game-main', ScoreAnagrameList.as_view(), name="score-anagram-list"),
    path('anagram-game-main', AnagramGameView.as_view(), name='anagram-game-main'),
    #path('anagram-game-main/<slug>/', AnagramGameDetailView.as_view(), name='detail'),
    path('anagram-score', ScoreAnagramView.as_view(), name='anagram-score'),
    path('anagram-game-main/create/', ScoreAnagramCreateView.as_view(), name='create'),
    
]