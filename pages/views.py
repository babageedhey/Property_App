from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.static import static


# Create your views here.

def index(request):

    return render(request, 'pages/index.html')

def about(request):

    return render(request, 'pages/about.html')
