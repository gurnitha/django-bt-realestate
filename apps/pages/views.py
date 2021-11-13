# apps/pages/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.listings.models import Listing

# Create your views here.

def home(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
	context = {'listings':listings}
	return render(request, 'pages/index.html', context)

def about(request):
	return render(request, 'pages/about.html')
