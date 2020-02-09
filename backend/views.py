from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
import BuildStoresDictionary as build

# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def gui(request):
    return HttpResponse("This is the GUI for Test")

def run(request):
    return HttpResponse(str(build.build_stores_dict(build.get_stores_list())))