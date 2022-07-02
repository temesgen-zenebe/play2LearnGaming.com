from django.urls import path

from .views import AnagramGameView,ScoreAnagramGameView

app_name = 'anagramGame'
urlpatterns = [
    path('anagram-game', AnagramGameView.as_view(), name='anagram-game'),
    path('anagram-score', ScoreAnagramGameView.as_view(), name='anagram-score'),
]