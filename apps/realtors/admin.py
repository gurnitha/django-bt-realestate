# apps/realtors/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.realtors.models import Realtor  

# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
	list_display = ('id','name','photo','phone','email', 'hire_date', 'is_mvp')
	list_display_links = ('id', 'name')
	list_filter = ('is_mvp',)
	list_editable = ('is_mvp',)
	search_fields = ('name','phone','email')
	list_per_page = 2


admin.site.register(Realtor, RealtorAdmin)
