from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
# Create your views here.


class HomeView(ListView):
    model = User
    template_name = 'base.html'


class IndexView(TemplateView):
    template_name = "index.html"


class PortfolioView(TemplateView):
    template_name = "new_design/portfolio.html"


class AboutView(TemplateView):
    template_name = "new_design/about.html"
