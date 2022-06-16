from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib import messages


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


class ProfileUpdateView(generic.UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'registration/update_profile.html'

    def get_object(self, queryset=None):
        return self.request.user
