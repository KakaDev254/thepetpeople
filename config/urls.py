from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('events/', include('events.urls')),
    path('gallery/', include('gallery.urls')),
    path('shop/', include('shop.urls')),
]
