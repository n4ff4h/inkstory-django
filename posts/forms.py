from statistics import mode
from django import forms
from .models import Post
from taggit.forms import TagWidget, TagField
from tinymce.widgets import TinyMCE


class PostCreateForm(forms.ModelForm):
    tags = TagField(help_text="",
                    widget=TagWidget(attrs={'placeholder': 'Eg: food, entertainment, sports',
                                            'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                                     'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                                     'focus:border-blue-500'}), )
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ('title', 'slug', 'tags', 'header_image', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                                     'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                                     'focus:border-blue-500'}),

            'slug': forms.TextInput(attrs={'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                                    'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                                    'focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 '
                                                    'dark:placeholder-gray-400 dark:text-white '
                                                    'dark:focus:ring-blue-500 dark:focus:border-blue-500'}),

            'header_image': forms.FileInput(
                attrs={'class': 'block mb-4 w-full text-sm text-gray-900 bg-gray-50 rounded-lg '
                                'border border-gray-300 cursor-pointer '
                                'focus:outline-none'}),

            'snippet': forms.Textarea(
                attrs={'rows': '4', 'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                             'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                             'focus:border-blue-500'}),
        }


class PostUpdateForm(forms.ModelForm):
    tags = TagField(help_text="",
                    widget=TagWidget(attrs={'placeholder': 'Eg: food, entertainment, sports',
                                            'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                                     'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                                     'focus:border-blue-500'}), )

    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ('title', 'slug', 'tags', 'header_image', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border border-gray-300 sm:text-xs '
                         'focus:ring-blue-500 focus:border-blue-500'}),

            'slug': forms.TextInput(attrs={'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                                    'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                                    'focus:border-blue-500'}),

            'header_image': forms.FileInput(
                attrs={'class': 'block mb-4 w-full text-sm text-gray-900 bg-gray-50 rounded-lg '
                                'border border-gray-300 cursor-pointer'
                                'focus:outline-none'}),

            'snippet': forms.Textarea(
                attrs={'rows': '4', 'class': 'block p-2 mb-4 w-full text-gray-900 bg-gray-50 rounded-lg border '
                                             'border-gray-300 sm:text-xs focus:ring-blue-500 '
                                             'focus:border-blue-500'}),
        }
