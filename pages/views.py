from typing import ValuesView
from django.views.generic import TemplateView
from django.views import View
from multiprocessing import context
from urllib import request
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from anagram_game.models import Anagram_score
from math_game.models import Addition_score,Division_score,Multiplication_score,Subtraction_score


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'

class PrintGameScore(View):
    def get(self, request):
        #operate10 = Addition_score.objects.filter(Q(user = request.user) & Q(max_range = 10)).order_by('-point')
        operate1 = Addition_score.objects.all().order_by('-point').distinct('point')
        operate2 = Division_score.objects.all().order_by('-point').distinct('point')
        operate3=  Multiplication_score.objects.all().order_by('-point').distinct('point')
        operate4 = Subtraction_score.objects.all().order_by('-point').distinct('point')
        anagramScore = Anagram_score.objects.all().order_by('-point').distinct('point')
        context = {
            'Addition':operate1,
            'Division':operate2,
            'Multiplication':operate3,
            'Subtraction':operate4,
            'anagramScore':anagramScore
        }
        return render(request, 'pages/home.html', context)

