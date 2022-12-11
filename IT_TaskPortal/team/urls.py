from django.urls import path

from IT_TaskPortal.team.views import TeamListView, EmployeeDetailsView

urlpatterns =[
    path('', TeamListView.as_view(),name='the team'),
    path('details/<int:pk>', EmployeeDetailsView.as_view(), name='employee details'),
]