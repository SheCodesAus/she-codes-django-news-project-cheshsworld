from distutils.command.upload import upload
from time import timezone
from unicodedata import category
from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    # foreign key references the user
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    pub_update = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image_upload = models.URLField(default="https://picsum.photos/600")
    category = models.ForeignKey(
        Category,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'stories'
    )
    
    def __str__(self):
        return f"{self.pub_date} - {self.title}"
