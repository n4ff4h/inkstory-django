from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView, UpdatePostView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # pk: primary key of the model which is passed into the view
    path('posts/<slug:slug>/', PostDetailView.as_view(), name="post-detail"),
    path('create/', CreatePostView.as_view(), name="create"),
    path('posts/edit/<slug:slug>/', UpdatePostView.as_view(), name="update"),
    path('delete/<int:pk>/', views.delete_post, name="delete"),
]
