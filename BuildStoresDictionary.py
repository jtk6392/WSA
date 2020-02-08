
from urllib import request
from urllib import parse
import http.client
import json
from uszipcode import SearchEngine

KEY="d417eac4aaa24bc082c1581ef13783ea&api"

def get_stores_list():
    """
    Queries Wegman's api for the information on their stores and reads the response
    :return: list of wegmans stores and their data
    """
    web_respone=request.urlopen("https://api.wegmans.io/stores?Subscription-Key=%s-version=2018-10-18" % KEY)
    store_json=http.client.HTTPResponse.read(web_respone)
    return json.loads(store_json)["stores"]

def build_stores_dict(list):
    """
    Takes a list of stores and build a dictionary of store numbers based on zipcodes
    :param list:(List) list of all the stores and their data
    :return: store_dict(dict): a dictionary of all the store numbers indexed by zipcodes
    """
    store_dict={}
    for store in list:
        lat=store["latitude"]
        long=store["longitude"]
        number=store["number"]
        zipcodes=SearchEngine().by_coordinates(lat, long, returns=2)

        for entry in zipcodes:
            if entry.zipcode not in store_dict.keys():
                store_dict[entry.zipcode]=[number]
            else:
                store_dict[entry.zipcode].append(number)
    return store_dict

def get_product(product):
    """
    Finds products matching the users search that wegmans sells
    :param product:(String) the name of the product we are looking for
    :return:(list) a list of tuples containing the products name and sku respectively
    """
    product=parse.quote(product)
    web_respone = request.urlopen("https://api.wegmans.io/products/search?query=%s&api-version=2018-10-18&subscription-key=%s" % (product, KEY))
    product_json = http.client.HTTPResponse.read(web_respone)
    return make_product(json.loads(product_json)["results"])

def make_product(list):
    """
    takes a list of matching products and makes a tuple of the products name and sku for each product
    :param list:(list) list of product data
    :return:(list) list of tuples of the products
    """
    available_products=[]
    for entry in list:
        available_products.append((entry['name'], entry['sku']))
    return available_products


print(get_product("ground beef"))
print(build_stores_dict(get_stores_list()))