from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from IT_TaskPortal.core.utils import get_task_new_user_by_username_task_pk
from IT_TaskPortal.tasks.forms import NewUserTaskCreateForm, EditTaskForNewUser
from IT_TaskPortal.tasks.models import Buildings, TaskForNewWorker, ExternalTelekomTasks

UserModel = get_user_model()


# Create your views here.

@login_required
def add_task_for_new_user(request):
    if request.method == 'GET':
        form = NewUserTaskCreateForm()
    else:
        form = NewUserTaskCreateForm(request.POST)
        if form.is_valid():
            task_new_user = form.save(commit=False)
            task_new_user.user = request.user
            task_new_user.save()
            return redirect('user-profile details', pk=request.user.pk)
    context = {
        'form': form,

    }
    return render(request, 'tasks/task-new-user.html', context)


def task_new_user_details(request, username, pk):
    task_new_user = get_task_new_user_by_username_task_pk(pk)
    owner = UserModel.objects.get(username=task_new_user.user.username)
    if request.method == 'GET':
        form = EditTaskForNewUser(instance=task_new_user)
    else:
        form = EditTaskForNewUser(request.GET, instance=task_new_user)
    context = {
        'pk': task_new_user.pk,
        'owner': owner,
        'task_new_user': task_new_user,
        'form': form,
    }

    return render(request, 'tasks/task-new-user-detail-page.html', context)


def edit_task_for_new_user(request, pk):
    task_new_user = get_task_new_user_by_username_task_pk(pk)
    if request.method == 'GET':
        form = EditTaskForNewUser(instance=task_new_user)
    else:
        form = EditTaskForNewUser(request.POST, instance=task_new_user)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile details', username, pk)
    context = {
        'form': form,
        #     'username': username,
        #     'pet_slug': pet_slug,
    }
    # return render(request, 'pets/pet-edit-page.html', context)
    return render(request, 'tasks/task-new-user-detail-page.html', context)


class SeeBuildingsView(ListView):
    template_name = "tasks/buildings/building-page.html"
    model = Buildings
    context_object_name = 'buildings'


from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda user: user.is_staff)
def staff_place_for_statistic(request):
    all_tasks = TaskForNewWorker.objects.all()
    in_progress = 'В прогрес'
    pending = 'Очаква изпълнение'
    partial_executed = 'Частично изпълненa'
    close = 'Приключена'
    external_tasks = ExternalTelekomTasks.objects.all()

    context = {
        'all_tasks': all_tasks,
        'closed_tasks': all_tasks.filter(status=in_progress),
        'in_progress_tasks': all_tasks.filter(is_new_worker=True),
        'partial_executed_tasks': TaskForNewWorker.objects.all().filter(status=partial_executed),
        'pending_tasks': TaskForNewWorker.objects.all().filter(status=pending),
        'external_tasks': external_tasks,
    }

    return render(request, 'tasks/management-page.html', context)


"""
 open = 'Нов'
    in_progress = 'В прогрес'
    pending = 'Очаква изпълнение'
    partial_executed = 'Частично изпълненa'
    close = 'Приключена'
"""


class ExternalTelekomTaskView(DetailView):
    model = ExternalTelekomTasks
    context_object_name = 'external_task'
    template_name = 'tasks/telecom-task-details.html'

class ExternalTelekomTaskProtocl(DetailView):
    model = ExternalTelekomTasks
    context_object_name = 'external_task'
    template_name = 'tasks/telecom-task-protocol.html'