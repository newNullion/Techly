from django.shortcuts import render
from django.views.generic import TemplateView



class MainView(TemplateView):
    template_name = 'main.html'