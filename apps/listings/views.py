# apps/listings/views.py

# Django modules
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# locals
from apps.listings.models import Listing

# Create your views here.

def listing_list(request):
	# listings = Listing.objects.all()
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)

	# Get 3 listings objects per page
	paginator = Paginator(listings, 3)
	# Passing the url parameter 'page' to the GET method
	page = request.GET.get('page')
	# Get the page
	page_listings = paginator.get_page(page)

	context = {
		# 'listings':listings,
		'listings':page_listings
	}
	return render(request, 'listings/listing_list.html', context)

def listing_detail(request, listing_id):
	listing = get_object_or_404 (Listing, pk=listing_id)
	print(listing)
	context = {'listing':listing}
	return render(request, 'listings/listing_detail.html', context)
