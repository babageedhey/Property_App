from django.contrib import admin
from . models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links = ('id', 'title','realtor')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description','address', 'city','state', 'zipcode')
    list_per_page = 15
# Register your models here.
admin.site.register(Listing, ListingAdmin)