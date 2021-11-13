# apps/listings/views.py

# Django modules
from django.shortcuts import render, get_object_or_404

# locals
from apps.listings.models import Listing

# Create your views here.

def listing_list(request):
	listings = Listing.objects.all()
	context = {'listings':listings}
	return render(request, 'listings/listing_list.html', context)

def listing_detail(request, listing_id):
	listing = get_object_or_404 (Listing, pk=listing_id)
	print(listing)
	context = {'listing':listing}
	return render(request, 'listings/listing_detail.html', context)
