import email
from typing import ValuesView
from django.views.generic import TemplateView,CreateView,ListView
from django.views import View
from multiprocessing import context
from urllib import request
from django.urls import reverse_lazy,reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from anagram_game.models import Anagram_score,Comment_Anagram
from math_game.models import Addition_score,Division_score,Multiplication_score,Subtraction_score,Comment_math
from anagram_game.forms import CommentAnagrameForm
from math_game.forms import CommentForm  
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
    

class MyCommentsListView(View):
     
     def get(self, request):
         ana_comment = Comment_Anagram.objects.filter(Q(user = request.user) & Q(active = True)).order_by('-created').distinct('created')
         math_comment = Comment_math.objects.filter(Q(user = request.user) & Q(active = True)).order_by('-created').distinct('created')
         context = {
             'my_anagram_comment' : ana_comment,
             'my_math_comment': math_comment,  
         }
         return render(request, 'pages/my_comment.html', context)
     
     def post(self, request):
        game = request.POST.get('game_type')
        print(game)
        if game == 'anagrame':# anagrame game
            data = {  
                'game_type' : request.POST.get('game_type'),
                'comment' : request.POST.get('comment'), 
            }
            forms = CommentAnagrameForm(data)
            if forms.is_valid():
                commentNew = Comment_Anagram.objects.create(
                    user = request.user,
                    game_type = request.POST.get('game_type'),
                    comment = request.POST.get('comment'), 
                )
                commentNew.save()
                return redirect('pages:my_comment')
            else:   
                return render(request,"pages/my_comment.html",{})
        
        else:# math game
            data = {  
                'game_type' : request.POST.get('game_type'),
                'comment' : request.POST.get('comment'), 
            }
            forms = CommentForm(data)
            if forms.is_valid():
                commentNew = Comment_math.objects.create(
                    user = request.user,
                    game_type = request.POST.get('game_type'),
                    comment = request.POST.get('comment'), 
                )
                commentNew.save()
                return redirect('pages:my_comment')
            else:   
                return render(request,"pages/my_comment.html",{})

class GameCommentListView(ListView):
   template_name = 'pages/home.html'
   model = Games_comment
   context_object_name = 'games_comment'

   def get_queryset(self):
       comment = Games_comment.objects.filter(Q(active = True)).order_by('-created').distinct('created')
       return comment
    
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
        

    
