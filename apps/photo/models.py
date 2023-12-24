from django.db import models
import os

class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/uploads/')
    description = models.TextField()

    def delete(self, *args, **kwargs):
        # Get the image path
        image_path = self.image.path
        
        # Ensure the file exists before attempting deletion
        if os.path.exists(image_path):
            try:
                # Attempt to remove the file
                os.remove(image_path)
            except Exception as e:
                # Handle any exceptions during file deletion
                print(f"Error deleting file: {str(e)}")

        # Call the parent delete method after handling the file
        super(Photo, self).delete(*args, **kwargs)
