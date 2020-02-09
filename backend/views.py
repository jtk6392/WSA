from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
import BuildStoresDictionary as build

# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def application(request):
    template = loader.get_template("application.html")
    return HttpResponse(template.render())