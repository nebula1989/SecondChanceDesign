# admin.py
from django.conf import settings
from django.contrib import admin
from .models import Photo
from .forms import PhotoForm

class PhotoAdmin(admin.ModelAdmin):
    form = PhotoForm

    list_display = ['title', 'image_display', 'description']

    def image_display(self, obj):
        if obj.image:
            return '<img src="{}{}" width="100px" />'.format(settings.MEDIA_URL, obj.image)
        return 'No Image'

    image_display.allow_tags = True


admin.site.register(Photo, PhotoAdmin)
