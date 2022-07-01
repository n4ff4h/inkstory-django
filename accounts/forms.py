from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=255,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'input-field'}))

    last_name = forms.CharField(max_length=255,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'input-field'}))

    username = forms.CharField(max_length=255,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'input-field'}))

    email = forms.EmailField(max_length=255,
                             required=True,
                             widget=forms.EmailInput(attrs={'class': 'input-field'}))

    password1 = forms.CharField(max_length=255,
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'input-field'}))

    password2 = forms.CharField(max_length=255,
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'input-field'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class ProfileUpdateForm(UserChangeForm):
    first_name = forms.CharField(max_length=255,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'input-field'}))

    last_name = forms.CharField(max_length=255,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'input-field'}))

    username = forms.CharField(max_length=255,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'input-field'}))

    email = forms.EmailField(max_length=255,
                             required=True,
                             widget=forms.EmailInput(attrs={'class': 'input-field'}))

    password = forms.CharField(max_length=255,
                               widget=forms.PasswordInput(attrs={'class': 'input-field'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=255,
                                   required=True,
                                   widget=forms.PasswordInput(attrs={'class': 'input-field'}))

    new_password1 = forms.CharField(max_length=255,
                                    required=True,
                                    widget=forms.PasswordInput(attrs={'class': 'input-field'}))

    new_password2 = forms.CharField(max_length=255,
                                    required=True,
                                    widget=forms.PasswordInput(attrs={'class': 'input-field'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
