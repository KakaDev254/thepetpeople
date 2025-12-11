from django.shortcuts import render
from .models import GalleryImage

def gallery_list(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery/gallery.html', {'images': images})
