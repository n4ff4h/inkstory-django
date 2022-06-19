from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default_avatar.png', upload_to='profile_images')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
