# apps/listings/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.listings.models import Listing  

# Register your models here.

admin.site.register(Listing)