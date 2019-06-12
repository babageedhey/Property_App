from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.static import static
from listings.models import Listing
from listings.choices import *

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'prices': prices
    }

    return render(request, 'pages/index.html', context)

def about(request):

    return render(request, 'pages/about.html')
