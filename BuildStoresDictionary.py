
import http.client
import json
from urllib import parse
from urllib import request

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
        zipcodes=clean_zip_codes(SearchEngine().by_coordinates(lat, long, returns=1))

        for entry in zipcodes:
            if entry not in store_dict.keys():
                store_dict[entry]=[number]
            else:
                store_dict[entry].append(number)

    return store_dict

def get_product(product):
    """
    Finds products matching the users search that wegmans sells
    :param product:(String) the name of the product we are looking for
    :return:(list) a list of tuples containing the products name and sku respectively
    """
    product=parse.quote(product)
    web_respone = request.urlopen\
        ("https://api.wegmans.io/products/search?query=%s&api-version=2018-10-18&subscription-key=%s" % (product, KEY))
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

def clean_zip_codes(list):
    """
    takes the list of all the zip objects and just returns a list of the zipcodes
    :param list:(list) the list of zipcode objects
    :return:(list) the list of only zipcodes
    """
    zip_codes=[]
    for entry in list:
        zip_codes.append(entry.zipcode)
    return zip_codes

def locate_nearest_stores(dic, location):
    """
    collects zipcodes near you location and checks the dictionary  for wegmans in those locations. If no wegmans are
    found it checks again with a larger radius (25, 50, 75, 100). If no stores are found in an 100 mile radius it gives
     up
    :param dic:(dict) the dictionary of store locations
    :param location:(dict) the users latitude and longitude
    :return:(set) returns the set of stores in the area, -1 if nothing within 100 miles
    """
    for i in range(1, 5):
        zips=clean_zip_codes(SearchEngine().by_coordinates(location["lat"], location["lng"], radius=25*i, returns=1000))
        stores=locate_helper(zips, dic)
        if len(stores)>0:
            return stores
    return -1

def locate_helper(list, dic):
    """
    compares list of zipcodes to entries in the dictionary
    :param list:(list) the list of all the zipcodes near the use
    :param dic:(dict) the dictionary of store locations
    :return: the set of stores within the users area
    """
    stores=[]
    for zip in list:
        if zip in dic.keys():
            stores.extend(dic[zip])
    return stores

def shelf_location(store_num, sku):
    """
    Gets the items shelf location from the store number and sku
    :param store_num:(String) the stores number
    :param sku:(String) the sku number of the product
    :return: the shelf location of the product
    """
    web_respone = request.urlopen(
        "https://api.wegmans.io/products/%s/locations/%s?api-version=2018-10-18&subscription-key=%s" % (sku, store_num, KEY))
    location=http.client.HTTPResponse.read(web_respone)
    return json.loads(location)["locations"][0]["name"]

def get_price(store_num, sku):
    """
    gets the products price from its sku and store number
    :param store_num:(String) the stores number
    :param sku:(String) the sku number of the product
    :return: the price of the product
    """
    web_respone = request.urlopen(
        "https://api.wegmans.io/products/%s/prices/%s?api-version=2018-10-18&subscription-key=%s" % (sku, store_num, KEY))
    location = http.client.HTTPResponse.read(web_respone)
    return json.loads(location)["price"]
