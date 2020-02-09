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
    response = json.dumps(locate_nearest_stores(build_stores_dict(get_stores_list()), json.loads(body)))
    return HttpResponse(response)


@csrf_exempt
def get_item_from_name(request):
    body = request.body
    product = get_product(str(json.loads(body)))
    dct = dict()
    dct['name'] = product[0][0]
    dct['sku'] = product[0][1]
    response = json.dumps(dct)
    print(response)
    return HttpResponse(response)


@csrf_exempt
def get_price_location(request):
    data = dict()
    body = request.body
    info = json.loads(body)
    num = info['store_number']
    sku = info['sku']
    data['price'] = get_price(info['store_number'], info['sku'])
    print(data)
    data['location'] = shelf_location(num, sku)
    response = json.dumps(data)
    return HttpResponse(response)

