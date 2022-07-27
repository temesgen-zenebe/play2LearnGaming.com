from multiprocessing import context
from urllib import request
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Math_score
from .forms import MathScoreForm
# Create your views here.

class MathGameView(ListView):
    model = Math_score
    template_name = 'math_game/math_main.html'
    context_object_name  = 'mathScore'
    paginate_by: 10

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


def ScoreMathForm(request):
    if request.method == 'POST':
        #user = request.user
        operator=request.POST.get('operator')
        max_range=request.POST.get('max_range')
        score=request.POST.get('score')
        point=request.POST.get('point')
        ranked=request.POST.get('ranked')
        print(score)
        new = Math_score(operator=operator,max_range=max_range ,score=score, point=point ,ranked=ranked)
        new.save()
    return render(request,"math_game/math_main.html")