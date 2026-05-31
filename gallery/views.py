from django.shortcuts import render, get_object_or_404
from .models import GalleryImage

def gallery_list(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery/gallery.html', {'gallery_images': images})

# Optional: Add a detail view for individual images
def gallery_detail(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    return render(request, 'gallery/gallery_detail.html', {'gallery_image': image})