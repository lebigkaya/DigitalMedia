from django.db import models

class MusicFile(models.Model):
    file = models.FileField(upload_to='music/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class VideoFile(models.Model):
    file = models.FileField(upload_to='video/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
