from django.db import models
from django.urls import reverse

class Video(models.Model):

    PLATFORM = ( 
    ('Youtube'),
    ('Twitch'),
    ('Tiktok'),
    ('Instagram'),
    ('Twitter'),
    ('Other'),
    )

    url = models.CharField(max_length=200)
    description = models.Charfield(max_length=200,blank=True)
    platform = models.CharField(max_length=200,choices=PLATFORM)
    videos = models.Manager()

    def __str__(self):
        return self.url
    
    def get_absolute_url(self):
        return reverse('video-detail',args=[str(self.id)])
