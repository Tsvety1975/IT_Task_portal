from django.views import generic as views
from django.shortcuts import render

# Create your views here.

class IndexView(views.TemplateView):
    template_name = 'common/index.html'

