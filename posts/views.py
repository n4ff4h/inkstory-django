# Note: ListView is used to get all the post records
#       while DetailView is used to get just one record
#       from the database.

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostCreateForm, PostUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from taggit.models import Tag
from django.views.decorators.csrf import requires_csrf_token
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, slug=self.kwargs['slug'])

        liked = False
        # If the user liked the post
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        total_likes = post.total_likes()
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


@method_decorator(login_required(login_url='/registration/login'), name='dispatch')
class CreatePostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'create_post.html'

    # Save logged-in user as post author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePostView, self).form_valid(form)


@method_decorator(login_required(login_url='/registration/login'), name='dispatch')
class UpdatePostView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'update_post.html'


@requires_csrf_token
def upload_image_view(request):
    f = request.FILES['image']
    fs = FileSystemStorage()
    file_name = str(f).split('.')[0]
    file = fs.save(file_name, f)
    file_url = fs.url(file)

    return JsonResponse({'success': 1, 'file': {'url': file_url}})


@requires_csrf_token
def upload_file_view(request):
    f = request.FILES['file']
    fs = FileSystemStorage()
    file_name, ext = str(f).split('.')
    print(file_name, ext)
    file = fs.save(str(f), f)
    file_url = fs.url(file)
    file_size = fs.size(file)

    return JsonResponse({'success': 1, 'file': {'url': file_url, 'name': str(f), 'size': file_size}})


@requires_csrf_token
def upload_link_view(request):
    import requests
    from bs4 import BeautifulSoup

    print(request.GET['url'])
    url = request.GET['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    metas = soup.find_all('meta')
    description = ""
    title = ""
    image = ""
    for meta in metas:
        if 'property' in meta.attrs:
            if meta.attrs['property'] == 'og:image':
                image = meta.attrs['content']
        elif 'name' in meta.attrs:
            if meta.attrs['name'] == 'description':
                description = meta.attrs['content']
            if meta.attrs['name'] == 'title':
                title = meta.attrs['content']
    return JsonResponse({'success': 1, 'meta': {"description": description, "title": title, "image": {"url": image}}})


# uid is post user id
# pk is post primary key
def delete_post(request, uid, pk):
    # check if post author id matches logged-in users id
    if uid == request.user.id:
        post = Post.objects.get(pk=pk)
        post.delete()
    return redirect('home')


def tags_view(request, tag):
    # Filter tags from the tag parameter passed from url
    tags = Tag.objects.filter(slug=tag).values_list('name', flat=True)
    # Filter posts based on tags
    posts = Post.objects.filter(tags__name__in=tags)

    return render(request, 'tag_posts.html', {'tag': tag, 'posts': posts})


def like_view(request, pk):
    # Look up posts by post_id and assign it to post variable
    post = get_object_or_404(Post, id=pk)
    # If the user liked the post
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)  # unlike
    else:
        post.likes.add(request.user)  # like
    post.save()
    return render(request, 'partials/likes_section.html', context={'post': post})
