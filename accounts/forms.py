from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=255,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 '
                                                                        'text-gray-900 text-sm rounded-lg '
                                                                        'focus:ring-blue-500 focus:border-blue-500 '
                                                                        'block w-full p-2.5 dark:bg-gray-700 '
                                                                        'dark:border-gray-600 '
                                                                        'dark:placeholder-gray-400 dark:text-white '
                                                                        'dark:focus:ring-blue-500 '
                                                                        'dark:focus:border-blue-500'}))

    last_name = forms.CharField(max_length=255,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 '
                                                                       'text-gray-900 text-sm rounded-lg '
                                                                       'focus:ring-blue-500 focus:border-blue-500 '
                                                                       'block w-full p-2.5 dark:bg-gray-700 '
                                                                       'dark:border-gray-600 '
                                                                       'dark:placeholder-gray-400 dark:text-white '
                                                                       'dark:focus:ring-blue-500 '
                                                                       'dark:focus:border-blue-500'}))

    username = forms.CharField(max_length=255,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 '
                                                                      'text-gray-900 text-sm rounded-lg '
                                                                      'focus:ring-blue-500 focus:border-blue-500 '
                                                                      'block w-full p-2.5 dark:bg-gray-700 '
                                                                      'dark:border-gray-600 '
                                                                      'dark:placeholder-gray-400 dark:text-white '
                                                                      'dark:focus:ring-blue-500 '
                                                                      'dark:focus:border-blue-500'}))

    email = forms.EmailField(max_length=255,
                             required=True,
                             widget=forms.EmailInput(attrs={'class': 'bg-gray-50 border border-gray-300 '
                                                                     'text-gray-900 text-sm rounded-lg '
                                                                     'focus:ring-blue-500 focus:border-blue-500 '
                                                                     'block w-full p-2.5 dark:bg-gray-700 '
                                                                     'dark:border-gray-600 '
                                                                     'dark:placeholder-gray-400 dark:text-white '
                                                                     'dark:focus:ring-blue-500 '
                                                                     'dark:focus:border-blue-500'}))

    password1 = forms.CharField(max_length=255,
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'bg-gray-50 border border-gray-300 '
                                                                           'text-gray-900 text-sm rounded-lg '
                                                                           'focus:ring-blue-500 focus:border-blue-500 '
                                                                           'block w-full p-2.5 dark:bg-gray-700 '
                                                                           'dark:border-gray-600 '
                                                                           'dark:placeholder-gray-400 dark:text-white '
                                                                           'dark:focus:ring-blue-500 '
                                                                           'dark:focus:border-blue-500'}))

    password2 = forms.CharField(max_length=255,
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'bg-gray-50 border border-gray-300 '
                                                                           'text-gray-900 text-sm rounded-lg '
                                                                           'focus:ring-blue-500 focus:border-blue-500 '
                                                                           'block w-full p-2.5 dark:bg-gray-700 '
                                                                           'dark:border-gray-600 '
                                                                           'dark:placeholder-gray-400 dark:text-white '
                                                                           'dark:focus:ring-blue-500 '
                                                                           'dark:focus:border-blue-500'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ProfileUpdateForm(UserChangeForm):
    first_name = forms.CharField(max_length=255,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 '
                                                                        'text-gray-900 text-sm rounded-lg '
                                                                        'focus:ring-blue-500 focus:border-blue-500 '
                                                                        'block w-full p-2.5 dark:bg-gray-700 '
                                                                        'dark:border-gray-600 '
                                                                        'dark:placeholder-gray-400 dark:text-white '
                                                                        'dark:focus:ring-blue-500 '
                                                                        'dark:focus:border-blue-500'}))

    last_name = forms.CharField(max_length=255,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 '
                                                                       'text-gray-900 text-sm rounded-lg '
                                                                       'focus:ring-blue-500 focus:border-blue-500 '
                                                                       'block w-full p-2.5 dark:bg-gray-700 '
                                                                       'dark:border-gray-600 '
                                                                       'dark:placeholder-gray-400 dark:text-white '
                                                                       'dark:focus:ring-blue-500 '
                                                                       'dark:focus:border-blue-500'}))

    username = forms.CharField(max_length=255,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 '
                                                                      'text-gray-900 text-sm rounded-lg '
                                                                      'focus:ring-blue-500 focus:border-blue-500 '
                                                                      'block w-full p-2.5 dark:bg-gray-700 '
                                                                      'dark:border-gray-600 '
                                                                      'dark:placeholder-gray-400 dark:text-white '
                                                                      'dark:focus:ring-blue-500 '
                                                                      'dark:focus:border-blue-500'}))

    email = forms.EmailField(max_length=255,
                             required=True,
                             widget=forms.EmailInput(attrs={'class': 'bg-gray-50 border border-gray-300 '
                                                                     'text-gray-900 text-sm rounded-lg '
                                                                     'focus:ring-blue-500 focus:border-blue-500 '
                                                                     'block w-full p-2.5 dark:bg-gray-700 '
                                                                     'dark:border-gray-600 '
                                                                     'dark:placeholder-gray-400 dark:text-white '
                                                                     'dark:focus:ring-blue-500 '
                                                                     'dark:focus:border-blue-500'}))

    password = forms.CharField(max_length=255,
                               widget=forms.PasswordInput(attrs={'class': 'bg-gray-50 border border-gray-300 '
                                                                          'text-gray-900 text-sm rounded-lg '
                                                                          'focus:ring-blue-500 focus:border-blue-500 '
                                                                          'block w-full p-2.5 dark:bg-gray-700 '
                                                                          'dark:border-gray-600 '
                                                                          'dark:placeholder-gray-400 dark:text-white '
                                                                          'dark:focus:ring-blue-500 '
                                                                          'dark:focus:border-blue-500'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
