from django.db import models
import os

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/uploads/')
    description = models.TextField()

    def delete(self, *args, **kwargs):
        # Delete the file from the filesystem when the object is deleted
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super(Photo, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title