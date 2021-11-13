# apps/pages/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.listings.models import Listing
from apps.realtors.models import Realtor

# Create your views here.

def home(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
	context = {'listings':listings}
	return render(request, 'pages/index.html', context)

def about(request):
	# Get all the realtors
	realtors = Realtor.objects.order_by('-hire_date')

	# Get MVP
	mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

	context = {
		'realtors':realtors,
		'mvp_realtors':mvp_realtors
	}

	return render(request, 'pages/about.html', context)
