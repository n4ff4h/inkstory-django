from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    # model.CASCADE: will delete all posts related to the user, if user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # Redirect to post detail page for the specified post id
        return reverse('post-detail', args=(str(self.id)))
