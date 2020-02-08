from django.shortcuts import render
from django.http import HttpResponse
import BuildStoresDictionary as build

# Create your views here.

def gui(request):
    return HttpResponse("This is the GUI for Testing.")

def run(request):
    return HttpResponse(str(build.build_stores_dict(build.get_stores_list())))