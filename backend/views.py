from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gui(request):
    return HttpResponse("This is the GUI for Testing.")

def run(request):
    return HttpResponse("This is the running GUI.")