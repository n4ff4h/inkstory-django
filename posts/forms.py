from statistics import mode
from django import forms
from .models import Post
from taggit.forms import TagWidget, TagField
from froala_editor.widgets import FroalaEditor


class PostCreateForm(forms.ModelForm):
    tags = TagField(help_text="",
                    widget=TagWidget(attrs={'placeholder': 'Eg: food, entertainment, sports',
                                            'class': 'input-field'}), )

    body = forms.CharField(widget=FroalaEditor(options={
        'heightMin': '200'
    }))

    class Meta:
        model = Post
        fields = ('title', 'slug', 'tags', 'header_image', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field'}),

            'slug': forms.TextInput(attrs={'class': 'input-field'}),

            'header_image': forms.FileInput(
                attrs={'class': 'hidden', 'id': 'dropzone-file', 'type': 'file'}),

            'snippet': forms.Textarea(
                attrs={'rows': '4', 'class': 'input-field'}),
        }


class PostUpdateForm(forms.ModelForm):
    tags = TagField(help_text="",
                    widget=TagWidget(attrs={'placeholder': 'Eg: food, entertainment, sports',
                                            'class': 'input-field'}), )

    body = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Post
        fields = ('title', 'slug', 'tags', 'header_image', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'input-field'}),

            'slug': forms.TextInput(
                attrs={'class': 'input-field'}),

            'header_image': forms.FileInput(
                attrs={'class': 'hidden', 'id': 'dropzone-file', 'type': 'file'}),

            'snippet': forms.Textarea(
                attrs={'rows': '4', 'class': 'input-field'}),
        }
