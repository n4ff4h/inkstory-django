from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
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

    terms_and_privacy_policy = forms.BooleanField(
        required=True, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2', 'terms_and_privacy_policy']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'input-field'}))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'class': 'input-field'}))
    remember_me = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


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
