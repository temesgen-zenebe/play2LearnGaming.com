from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
import json

# Create your views here.
class AnagramView(TemplateView):
    template_name = 'anagram_game/anagram_main.html'
    
class ScoreAnagramView(TemplateView):
    template_name = 'anagram_game/anagram_score.html'

class jsonAnagrameList(View):    
    def get(self, request):
        with open('static/data/anagram.json', 'r') as f:
            my_json_obj = json.load(f)
            #json_data="hello world"
        context = {
            'json_data':my_json_obj
        }
        return render(request, 'anagram_game/anagram_main.html', context)