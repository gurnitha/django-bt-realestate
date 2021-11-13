# apps/listings/views.py

# Django modules
from django.shortcuts import render

# locals
from apps.listings.models import Listing

# Create your views here.

def listing_list(request):
	listings = Listing.objects.all()
	context = {'listings':listings}
	return render(request, 'listings/listing_list.html', context)
