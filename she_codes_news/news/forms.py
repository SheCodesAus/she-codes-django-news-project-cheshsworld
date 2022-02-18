from pyexpat import model
from django import forms    
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['image_upload', 'title','content', 'category']
        
    