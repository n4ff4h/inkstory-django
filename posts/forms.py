from statistics import mode
from django import forms
from .models import Post
from taggit.forms import TagWidget


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'tags', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                                     'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                                     'focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
                                                     'dark:placeholder-gray-400 dark:text-white '
                                                     'dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'slug': forms.TextInput(attrs={'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                                    'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                                    'focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
                                                    'dark:placeholder-gray-400 dark:text-white '
                                                    'dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'tags': TagWidget(attrs={'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                              'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                              'focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
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
        fields = ('title', 'slug', 'tags', 'body')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border border-gray-300 sm:text-xs '
                         'focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
                         'dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 '
                         'dark:focus:border-blue-500'}),
            'slug': forms.TextInput(attrs={'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                                    'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                                    'focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
                                                    'dark:placeholder-gray-400 dark:text-white '
                                                    'dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'tags': TagWidget(attrs={'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                              'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                              'focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
                                              'dark:placeholder-gray-400 dark:text-white '
                                              'dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'body': forms.Textarea(attrs={
                'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border border-gray-300 sm:text-xs '
                         'focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
                         'dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 '
                         'dark:focus:border-blue-500'}),
        }
