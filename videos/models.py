from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    youtube_id = models.CharField(max_length=11, verbose_name="YouTube ID", null=True, blank=True)
    vimeo_id = models.CharField(max_length=50, verbose_name="Vimeo ID", null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    song = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(upload_to='videos/static/images', null=True, blank=True)

    def __str__(self):
        return str(self.title)
