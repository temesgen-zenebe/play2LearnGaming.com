from multiprocessing import context
from operator import ge
from urllib import request
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views import View
from django.db.models import Q
from .models import Anagram_score
from .forms import AnagrameScoreForm
import json


# Create your views here.
class AnagramGameView(ListView):
    model = Anagram_score
    paginate_by: 10

class AnagramGameDetailView(DetailView):
    model = Anagram_score
    context_object_name = 'anagramScore'
    template_name = 'anagram_game/anagram_main.html'

class ScoreAnagramView(TemplateView):
    model = Anagram_score
    template_name = 'anagram_game/anagram_score.html'

class ScoreAnagramCreateView(CreateView):
    model = Anagram_score
    form_class = AnagrameScoreForm
    template_name = 'anagram_game/create_anagram_score.html'
    success_url = ''
    

class ScoreAnagrameList(View):

    def get(self, request):
       
        scoreAnagram = Anagram_score.objects.all().order_by('-point').distinct('point')
        
        with open('static/data/anagram.json', 'r') as f:
            my_json = json.load(f) #anagram json 

        context = {
            'json_data':my_json,
            'scoreAnagram':scoreAnagram,
        }
        return render(request, 'anagram_game/anagram_main.html', context)
   
    def post(self, request):
        wordSize=request.POST.get('word_size')
        if(wordSize):
            scoreNew = Anagram_score.objects.create(
                users = request.user,
                word_size=request.POST.get('word_size'),
                score=request.POST.get('score'),
                point=request.POST.get('point'),
             )
            scoreNew.save()
            return redirect('anagram_game:score-anagram-list')

class ScoreUserView(View):
    def get(self ,request):    
        userScoreAnagram = Anagram_score.objects.filter(Q(users = request.user)).order_by('-point').distinct('point') 
        context = { 'userScoreAnagram':userScoreAnagram}
        return render(request, 'anagram_game/anagram_score_list.html', context)

class ScoreView(View):
    def get(self ,request):    
        scoreAnagram = Anagram_score.objects.all().order_by('-point').distinct('point') 
        context = { 'Score_Anagram':scoreAnagram}
        return render(request, 'anagram_game/anagram_score.html', context)