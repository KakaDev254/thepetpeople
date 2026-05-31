from django.db import models
from cloudinary.models import CloudinaryField

class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    # Changed from ImageField to CloudinaryField
    image = CloudinaryField('image', folder='gallery/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title