from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views
from IT_TaskPortal.accounts.forms import CreateUserForm, EditUserForm
from IT_TaskPortal.tasks.models import TaskForNewWorker

# Create your views here.

UserModel = get_user_model()

class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = CreateUserForm
    success_url ='/'

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class SignInView(auth_views.LoginView):

   template_name = 'accounts/login-page.html'
   success_url = reverse_lazy('/')

class SignOutView(auth_views.LogoutView):
    template_name = 'accounts/sign-out.html'
    next_page = ('index')

class UserDetails(views.DetailView):
    model = UserModel
    template_name = 'accounts/user-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['task_new_users'] = TaskForNewWorker.objects.all()
        return context

class UserEditView(views.UpdateView):
    model = UserModel
    template_name = 'accounts/user-edit-page.html'
    form_class = EditUserForm

    def get_success_url(self):
        return reverse_lazy('user-profile details', kwargs={'pk': self.object.pk})


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/user-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = "accounts/password_reset_subject.txt"
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')

class MessageSendEmail(views.CreateView):
    template_name = 'accounts/users-home.html'


class ResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"

