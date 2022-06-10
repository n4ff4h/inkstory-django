from statistics import mode
from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                                     'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                                     'focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
                                                     'dark:placeholder-gray-400 dark:text-white '
                                                     'dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'author': forms.Select(attrs={'class': 'bg-gray-50 mb-4 border border-gray-300 text-gray-900 text-sm '
                                                   'rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full '
                                                   'p-2.5 dark:bg-gray-700 dark:border-gray-600 '
                                                   'dark:placeholder-gray-400 dark:text-white '
                                                   'dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'body': forms.Textarea(attrs={'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                                   'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                                   'focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
                                                   'dark:placeholder-gray-400 dark:text-white '
                                                   'dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border border-gray-300 sm:text-xs '
                         'focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
                         'dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 '
                         'dark:focus:border-blue-500'}),
            'body': forms.Textarea(attrs={
                'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border border-gray-300 sm:text-xs '
                         'focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
                         'dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 '
                         'dark:focus:border-blue-500'}),
        }
