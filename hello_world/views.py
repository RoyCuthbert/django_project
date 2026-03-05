from django.shortcuts import render
from django.http iport HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")