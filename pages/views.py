from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageViwe(TemplateView):
    template_name= 'home.html'


class AboutPageView(TemplateView):
    template_name= 'pages/about.html'

