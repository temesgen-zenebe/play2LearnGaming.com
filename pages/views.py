from django.views.generic import TemplateView
from multiprocessing import context
from urllib import request
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'



