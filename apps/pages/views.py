# apps/pages/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'pages/index.html')

def about(request):
	return render(request, 'pages/about.html')
