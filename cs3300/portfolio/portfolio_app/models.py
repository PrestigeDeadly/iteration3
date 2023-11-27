from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Video(models.Model):

    PLATFORM = ( 
    ('YT', 'Youtube'),
    ('TTV', 'Twitch'),
    ('TT', 'Tiktok'),
    ('IG', 'Instagram'),
    ('X', 'Twitter'),
    ('Other', 'Other'),
    )

    url = models.CharField(max_length=200)
    description = models.CharField(max_length=200,blank=True)
    platform = models.CharField(max_length=200,choices=PLATFORM)
    img = models.ImageField(null=True, blank=True, upload_to="images_")
    videos = models.Manager()

    def __str__(self):
        return self.url
    
    def get_absolute_url(self):
        return reverse('video-detail',args=[str(self.id)])