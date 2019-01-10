from django.contrib import admin
from . models import Realtor


class RealtorAdmin(admin.ModelAdmin):
     list_display = ('id','name','email', 'hire_date')
     list_display_links = ('id', 'name','hire_date')
     list_per_page = 20
     search_fields = ('name', 'hire_date')
     list_filter = ('name',)

# Register your models here.
admin.site.register(Realtor, RealtorAdmin)
