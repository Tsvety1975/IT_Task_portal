from django.urls import path, include

from IT_TaskPortal.tasks.views import add_task_for_new_user, task_new_user_details, edit_task_for_new_user, \
    SeeBuildingsView, staff_place_for_statistic, ExternalTelekomTaskView, ExternalTelekomTaskProtocl

urlpatterns = [
    path('add_new-user-task/', add_task_for_new_user, name='new-user task'),
    path('<str:username>/new_user-task/<int:pk>/', include([
        path('',task_new_user_details, name='new-user-task-details'),
        path('edit/', edit_task_for_new_user, name='edit-view'),
])),
    path('buildings/', SeeBuildingsView.as_view(), name='buildings'),
    path('management/', staff_place_for_statistic, name='management-page'),
    path('telecom/<int:pk>/', ExternalTelekomTaskView.as_view(), name='telecom-task-details',),
    path('telecom/<int:pk>/', ExternalTelekomTaskProtocl.as_view(), name='telecom-task-protokol',),

]
from .signals import *