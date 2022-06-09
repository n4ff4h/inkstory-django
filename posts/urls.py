from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # pk: primary key of the model which is passed into the view
    path('posts/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('create/', CreatePostView.as_view(), name="create"),
    path('posts/edit/<int:pk>', UpdatePostView.as_view(), name="update"),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name="delete"),
]
