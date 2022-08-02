from django.urls import path
from .views import AnagramView,ScoreAnagramView,jsonAnagrameList
from .views import *

app_name = 'anagram_game' 

urlpatterns = [
    path('anagram-game-main', AnagramView.as_view(), name='anagram-game-main'),
    path('anagram-game-main/', jsonAnagrameList.as_view(), name="json-list"),
    path('anagram-score', ScoreAnagramView.as_view(), name='anagram-score'),
   
]