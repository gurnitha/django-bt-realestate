# apps/pages/urls.py

# Django modules
from django.urls import path

# Locals
from apps.pages import views  

# Appname
app_name = 'pages'

# Urls
urlpatterns = [
    path('', views.home, name='home'),
]
