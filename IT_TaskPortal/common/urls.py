from django.urls import path

from IT_TaskPortal.common.views import IndexView

urlpatterns=[
    path('', IndexView.as_view(), name='index')
]