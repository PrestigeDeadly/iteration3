from django.forms import ModelForm
from django import forms
from .models import Video

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields =('url', 'description', 'platform', 'img')
