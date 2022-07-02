from django.urls import path
from .views import UserRegisterView, CustomLoginView, ProfileUpdateView, UserPasswordChangeView
from .forms import LoginForm

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True,
         template_name='accounts/login.html', authentication_form=LoginForm), name="login"),
    path('update_profile/', ProfileUpdateView.as_view(), name="profile_update"),
    path('password/', UserPasswordChangeView.as_view()),
]
