from django.urls import path, include
from django.contrib.auth import views as auth_views

from IT_TaskPortal.accounts.views import SignUpView, SignInView, UserDetails, UserDeleteView, UserEditView, SignOutView, \
    ResetPasswordView, MessageSendEmail, ResetConfirm

urlpatterns = [
    path('register/', SignUpView.as_view(), name='sign up'),
    path('login/', SignInView.as_view(), name='sign in'),
    path('user-profile/<int:pk>/', include([
        path('',  UserDetails.as_view(), name='user-profile details'),
        path('edit/',UserEditView.as_view(), name='user edit'),

        path('delete-user/', UserDeleteView.as_view(), name='user delete'),
    ])),
    path('logout/', SignOutView.as_view(), name='sign out'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('reset_email_send/', MessageSendEmail.as_view(), name='users-home'),
    path('password-reset-confirm/<uidb64>/<token>/',
         ResetConfirm.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete')
]

from .signals import *
