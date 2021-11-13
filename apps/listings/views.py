# apps/listings/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def listing_list(request):
	return render(request, 'listings/listing_list.html')
