from django.urls import path
from .views import AnagramView,ScoreAnagramView


app_name = 'anagram_game'

urlpatterns = [
    path('anagram-game-main/', AnagramView.as_view(), name='anagram-game-main'),
    path('anagram-score', ScoreAnagramView.as_view(), name='anagram-score'),
    
]