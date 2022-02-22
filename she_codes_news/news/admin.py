from django.contrib import admin

from .models import Category, NewsStory

admin.site.register(NewsStory)
admin.site.register(Category)