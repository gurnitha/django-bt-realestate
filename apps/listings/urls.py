# apps/listings/urls.py

# Django modules
from django.urls import path

# Locals
from apps.listings import views  

# Appname
app_name = 'listings'

# Urls
urlpatterns = [
    path('listing-list', views.listing_list, name='listing_list'),
]
