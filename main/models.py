from django.db import models

# Create your models here.
class Youtube_data(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField()
    thumbnail = models.URLField(max_length=200)
    video_url = models.URLField(max_length=200)
    channel_title = models.CharField(max_length=100, default="None")
    channel_url = models.URLField(max_length=200, default="None")
    is_live = models.BooleanField(default=False)
