from __future__ import division
from ast import Not, operator
from multiprocessing.dummy import active_children
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from multiprocessing import context
from django import views
from django.conf import settings
from urllib import request
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.db.models import Q
from .models import Math_score
from .models import (
    Addition_score,
    Division_score,
    Multiplication_score,
    Subtraction_score,
    Comment_math,
)
from .forms import MathScoreForm,CommentForm
# Create your views here.

class MathGameView(ListView):
    model = Math_score
    template_name = 'math_game/math_main.html'
    context_object_name  = 'mathScore'
    paginate_by: 10
    
    def sorted_rank_list(self):
        qs = Math_score.objects.all()
        return qs

class MathScoreUserView(View):
    
    def get(self, request):
        operate1 = Addition_score.objects.filter(Q(user = request.user)).order_by('-point').distinct('point')
        operate2 = Division_score.objects.filter(Q(user = request.user)).order_by('-point').distinct('point')
        operate3 = Multiplication_score.objects.filter(Q(user = request.user)).order_by('-point').distinct('point')
        operate4 = Subtraction_score.objects.filter(Q(user = request.user)).order_by('-point').distinct('point')
        
        context = {
            'Addition':operate1,
            'Division':operate2,
            'Multiplication':operate3,
            'Subtraction':operate4, 
            
        }
        return render(request, 'math_game/math_score_list.html', context)

class MathGameDetailView(DetailView):
    model = Math_score
    context_object_name = 'mathScore'
    template_name = 'math_game/math_main.html'
  
class ScoreMathGameView(TemplateView):
    model = Math_score
    template_name = 'math_game/math_score.html'


class ScoreMathCreateView(CreateView):
    model = Math_score
    form_class = MathScoreForm
    template_name = 'math_game/create_math_score.html'
    success_url = ''

class commentCreateView(CreateView):
    model = Comment_math
    form_class = CommentForm
    template_name = 'math_game/math_score.html'
    success_url = reverse_lazy('my-comment')

def ScoreMathForm(request):
    
    if request.method == 'POST':
        user = request.user,
        operator=request.POST.get('operator')
        max_range=request.POST.get('max_range')
        score=request.POST.get('score')
        point=request.POST.get('point')
        new = Math_score(operator=operator,max_range=max_range ,score=score, point=point )
        new.save()
    return render(request,"math_game/math_main.html")


class ScoreMathList(View):

    def get(self, request):
        #operate10 = Addition_score.objects.filter(Q(user = request.user) & Q(max_range = 10)).order_by('-point')
        operate1 = Addition_score.objects.all().order_by('-point').distinct('point')
        operate2 = Division_score.objects.all().order_by('-point').distinct('point')
        operate3=  Multiplication_score.objects.all().order_by('-point').distinct('point')
        operate4 = Subtraction_score.objects.all().order_by('-point').distinct('point')
        context = {
            
            'Addition':operate1,
            'Division':operate2,
            'Multiplication':operate3,
            'Subtraction':operate4,
        }
        return render(request, 'math_game/math_main.html', context)
   
    def post(self, request):
        operator=request.POST.get('operator')

        match operator:
           case 'Addition[+]':
              scoreNew = Addition_score.objects.create(
                  user = request.user,
                  operator=request.POST.get('operator'),
                  max_range=request.POST.get('max_range'),
                  score=request.POST.get('score'),
                  point=request.POST.get('point'),
              )
              scoreNew.save()
              messages.success(request, f'{request.user} : your score was successfully saved!')
              return redirect('math_game:score-math-list')

           case 'Division[/]':
              scoreNew = Division_score.objects.create(
                  user = request.user,
                  operator=request.POST.get('operator'),
                  max_range=request.POST.get('max_range'),
                  score=request.POST.get('score'),
                  point=request.POST.get('point'),
              )
              scoreNew.save()
              messages.success(request, f'{request.user} : your score was successfully saved!')
              return redirect('math_game:score-math-list')

           case 'Multiplication[*]':
              scoreNew = Multiplication_score.objects.create(
                  user = request.user,
                  operator=request.POST.get('operator'),
                  max_range=request.POST.get('max_range'),
                  score=request.POST.get('score'),
                  point=request.POST.get('point'),
              )
              scoreNew.save()
              messages.success(request, f'{request.user} : your score was successfully saved!')
              return redirect('math_game:score-math-list')

           case 'Subtraction[-]':
              scoreNew = Subtraction_score.objects.create(
                  user = request.user,
                  operator=request.POST.get('operator'),
                  max_range=request.POST.get('max_range'),
                  score=request.POST.get('score'),
                  point=request.POST.get('point'),
              )
              scoreNew.save()
              messages.success(request, f'{request.user} : your score was successfully saved!')
              return redirect('math_game:score-math-list')


class AllScoreMathList(View):

    def get(self, request):
        
        #about games
        operate1 = Addition_score.objects.all().order_by('-point').distinct('point')
        operate2 = Division_score.objects.all().order_by('-point').distinct('point')
        operate3=  Multiplication_score.objects.all().order_by('-point').distinct('point')
        operate4 = Subtraction_score.objects.all().order_by('-point').distinct('point')
        
        #comment
        comment = Comment_math.objects.all().order_by('-created')
        context = {
            
            'Addition':operate1,
            'Division':operate2,
            'Multiplication':operate3,
            'Subtraction':operate4,
            'userComment':comment,
        }
        return render(request, 'math_game/math_score.html', context)   

    def post(self, request):
        commentNew = Comment_math.objects.create(
                  user = request.user,
                  game_type = request.POST.get('game_type'),
                  comment = request.POST.get('comment'), 
              )
        commentNew.save()
        messages.success(request, f'{request.user} : your comment was successfully submited!')
        return redirect('math_game:all-math-score')