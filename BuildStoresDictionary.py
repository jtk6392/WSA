
from urllib import request
import http.client
import json
from uszipcode import SearchEngine

def get_stores_list():
    """
    Queries Wegman's api for the information on their stores and reads the response
    :return: list of wegmans stores and their data
    """
    web_respone=request.urlopen("https://api.wegmans.io/stores?Subscription-Key=d417eac4aaa24bc082c1581ef13783ea&api-version=2018-10-18")
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