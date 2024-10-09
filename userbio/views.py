from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def userbio(request):
    return HttpResponse("Hello, Userbio!")