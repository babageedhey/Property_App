from django.contrib import admin
from . models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','listing','email','contact_date')
    list_display_links = ('id',)
    list_filter = ('name',)
    # list_editable = ('name','email', 'listing') #This allow you to be able to edit from the list
    search_fields = ('name', 'id','email','listing')
    list_per_page = 15

admin.site.register(Contact,  ContactAdmin)