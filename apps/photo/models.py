from django.db import models

class Photo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/uploads/')
    description = models.TextField()
