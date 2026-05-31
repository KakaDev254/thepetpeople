from django.db import models
from django.utils import timezone
from django.urls import reverse
from cloudinary.models import CloudinaryField

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    # Changed from ImageField to CloudinaryField
    featured_image = CloudinaryField('image', folder='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # No namespace here
        return reverse('post_detail', args=[self.slug])