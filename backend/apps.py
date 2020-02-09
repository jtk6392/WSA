from django.apps import AppConfig
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from BuildStoresDictionary import *


class BackendConfig(AppConfig):
    name = 'backend'


@csrf_exempt
def get_store(request):
    body = request.body

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
    
    return HttpResponse(response)


@csrf_exempt

def get_price_location_image(request):

    data = dict()
    body = request.body
    info = json.loads(body)
    num = info['store_number']
    sku = info['sku']

    data['name'] = info['name']
    data['price'] = get_price(num, sku)
    data['location'] = shelf_location(num, sku)
    data['image'] = get_image(sku)
    response = json.dumps(data)
    return HttpResponse(response)


@csrf_exempt
def get_products_list(request):
    body = request.body
    info = json.loads(body)
    prods = get_product(info)

    response = json.dumps(prods)
    return HttpResponse(response)



