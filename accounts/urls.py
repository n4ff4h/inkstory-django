from django.urls import path
from .views import UserRegisterView, ProfileUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('update_profile/', ProfileUpdateView.as_view(), name="profile_update"),
]
