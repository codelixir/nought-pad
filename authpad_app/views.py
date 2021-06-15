from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ChangePassForm


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        user = self.request.user
        if user.is_authenticated:
            return self.request.user
        else:
            return None


class ChangePassView(PasswordChangeView):
    form_class = ChangePassForm
    template_name = 'registration/change_pass.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        user = self.request.user
        if user.is_authenticated:
            return self.request.user
        else:
            return None
