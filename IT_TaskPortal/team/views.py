from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView

from IT_TaskPortal.team.models import Employees


# Create your views here.
class TeamListView(ListView):
    context_object_name = 'employees'
    model = Employees
    template_name = 'team/team.html'
    extra_context = {

        'title': 'It Team',
            }

class EmployeeDetailsView(DetailView):
    context_object_name = 'employee'
    model = Employees
    template_name = 'team/details.html'


