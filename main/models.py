from django.db import models

# Create your models here.
class Youtube_data(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField()
    thumbnail = models.URLField(max_length=200)
    video_url = models.URLField(max_length=200)

