# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Locals

urlpatterns = [
    # Pages
    path('', include('apps.pages.urls', namespace='pages')),

    # Listings
    path('', include('apps.listings.urls', namespace='listings')),

    # Admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)