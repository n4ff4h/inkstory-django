# Note: ListView is used to get all the post records
#       while DetailView is used to get just one record
#       from the database.

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostCreateForm, PostUpdateForm


# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'create_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'update_post.html'


# class DeletePostView(DeleteView):
#     model = Post
#     template_name = 'delete_post.html'
#     success_url = reverse_lazy('home')


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')
