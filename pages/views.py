import email
from typing import ValuesView
from django.views.generic import TemplateView,CreateView,ListView
from django.views import View
from multiprocessing import context
from urllib import request
from django.urls import reverse_lazy,reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from anagram_game.models import Anagram_score
from math_game.models import Addition_score,Division_score,Multiplication_score,Subtraction_score
from .models import Games_comment
from .forms import GameCommentForm
from django.core.exceptions import ValidationError
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'

class GameCommentListView(ListView):
   template_name = 'pages/home.html'
   model = Games_comment
   context_object_name = 'games_comment'

   def get_queryset(self):
       comment = Games_comment.objects.filter(Q(active = True)).order_by('-created').distinct('created')
       return comment
    
class GameCommentCreateView(CreateView):
    model = Games_comment
    form_class = GameCommentForm
    template_name = 'pages/home.html'
    success_url = reverse_lazy('games-comment') 

class PrintGameScore(View):
    def get(self, request):
        #operate10 = Addition_score.objects.filter(Q(user = request.user) & Q(max_range = 10)).order_by('-point')
        operate1 = Addition_score.objects.all().order_by('-point').distinct('point')
        operate2 = Division_score.objects.all().order_by('-point').distinct('point')
        operate3=  Multiplication_score.objects.all().order_by('-point').distinct('point')
        operate4 = Subtraction_score.objects.all().order_by('-point').distinct('point')
        anagramScore = Anagram_score.objects.all().order_by('-point').distinct('point')
        comment = Games_comment.objects.filter(Q(active = True)).order_by('-created').distinct('created')
        context = {
            'Addition':operate1,
            'Division':operate2,
            'Multiplication':operate3,
            'Subtraction':operate4,
            'anagramScore':anagramScore,
            'gameComment':comment,
        }
        return render(request, 'pages/home.html', context)
    
    def post(self, request):
        data = {  'email' : request.POST.get('email'),
                  'comment' : request.POST.get('comment'),
                }
        forms = GameCommentForm(data)
        if forms.is_valid():
            commentNew = Games_comment.objects.create(
                  user = request.user,
                  email = request.POST.get('email'),
                  comment = request.POST.get('comment'), 
              )
            commentNew.save()
            return redirect('pages:math-score-list')
        else:   
            return render(request,"pages/home.html",{})
        

    
