from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView, UpdatePostView, delete_post, tags_view, like_view, \
    upload_image_view, upload_file_view, upload_link_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # pk: primary key of the model which is passed into the view
    path('posts/<slug:slug>/', PostDetailView.as_view(), name="post_detail"),
    path('create/', CreatePostView.as_view(), name="post_create"),
    path('posts/edit/<slug:slug>/', UpdatePostView.as_view(), name="post_update"),
    path('delete/<int:uid>/<int:pk>/', delete_post, name="post_delete"),
    path('t/<str:tag>/', tags_view, name="tags"),
    path('like/<int:pk>', like_view, name="like_post"),
    path('image-upload/', csrf_exempt(upload_image_view)),
    path('file-upload/', csrf_exempt(upload_file_view)),
    path('linkfetching/', upload_link_view),
]
