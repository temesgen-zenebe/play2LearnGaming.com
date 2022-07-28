from multiprocessing import context
from django.conf import settings
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
    

    def sorted_rank_list(self):
        qs = Math_score.objects.all()
        return qs


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
    currentUser = Math_score.objects.filter(user = settings.AUTH_USER_MODEL.id)
    if request.method == 'POST':
        #user = currentUser
        operator=request.POST.get('operator')
        max_range=request.POST.get('max_range')
        score=request.POST.get('score')
        point=request.POST.get('point')
        new = Math_score(operator=operator,max_range=max_range ,score=score, point=point )
        new.save()
    return render(request,"math_game/math_main.html")


def Addition_filter(request, slug1, slug2):
    score_set =  Math_score.objects.filter(user=slug1)
    score = score_set.filter(operator=slug2).order_by('point')
    context = {
                'level': 'point',
                'scores': score,
                'listing': 'operator' + slug2 + ' from user' + slug1
    }
    return render(request,'math_game/math_main.html', context)