from django.apps import AppConfig
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from BuildStoresDictionary import *


class BackendConfig(AppConfig):
    name = 'backend'

@csrf_exempt
def get_store(request):
    body = request.body
    print(str(json.loads(body)))
    print(locate_nearest_stores(json.loads(body), json.loads(body)))
    return HttpResponse(body)
