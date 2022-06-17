from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('', include('posts.urls')),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/', include('accounts.urls')),
]
