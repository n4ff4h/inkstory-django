from django.urls import path
from .views import UserRegisterView, ProfileUpdateView, UserPasswordChangeView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('update_profile/', ProfileUpdateView.as_view(), name="profile_update"),
    path('password/', UserPasswordChangeView.as_view()),
]
