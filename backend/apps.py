"""
Handles the backend API calls from the frontend through POST and GET routes.
"""
from django.apps import AppConfig
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from BuildStoresDictionary import *


class BackendConfig(AppConfig):
    name = 'backend'


@csrf_exempt
def get_store(request):
    """
    POST endpoint, takes latitude and longitude as request parameters and returns a list of the nearest Wegmans
    locations
    :param request: HttpRequest containing latitude and longitude
    :return: A list of the nearest Wegmans locations
    """
    body = request.body
    response = json.dumps(locate_nearest_stores(build_stores_dict(get_stores_list()), json.loads(body)))
    return HttpResponse(response)


@csrf_exempt
def get_price_location_image(request):
    """
    Takes a product sku and a store number and returns a JSON of its name, price, location, and image.
    :param request: store number and sku for a product query
    :return: A JSON with a product's name, price, location, image.
    """
    print(2)
    data = dict()
    body = request.body
    info = json.loads(body)
    num = info['store_number']
    sku = info['sku']
    data['name'] = info['name']
    data['price'] = get_price(num, sku)
    data['location'] = shelf_location(num, sku)
    images = get_image(sku)
    if images is not None and len(images) > 0:
        data['images'] = images['images']
    response = json.dumps(data)
    return HttpResponse(response)


@csrf_exempt
def get_products_list(request):
    """
    Returns a list of products similar to a given input string
    :param request: contains an input string to query Wegmans' database.
    :return: a list of products similar to the input string.
    """
    print(3)
    body = request.body
    info = json.loads(body)
    prods = get_product(info)

    response = json.dumps(prods)
    return HttpResponse(response)


