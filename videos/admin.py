from django.contrib import admin

# Register your models here.
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    actions_on_bottom = True

admin.site.register(Video, VideoAdmin)
