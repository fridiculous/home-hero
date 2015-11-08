import requests
import pandas as pd
import json


headers = {
    'cache-control': "no-cache",
    }

def _get_response(url, querystring):
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


def get_approved_venders():
    url = "https://rets.io/api/v1/vendors/approved"
    querystring = {"access_token":"09d66e16b29cdd623dd1e7d0d0f1f062"}
    return _get_response(url, querystring)


def get_arizona_transactions():
    url = "https://rets.io/api/v1/armls/transactions"
    querystring = {"access_token":"09d66e16b29cdd623dd1e7d0d0f1f062"}
    return _get_response(url, querystring)


def get_arizona_listings(limit=100, offset=0):
    url = "https://rets.io/api/v1/armls/listings"
    querystring = {
        "access_token":"09d66e16b29cdd623dd1e7d0d0f1f062",
        "state[in][0]":"AZ","limit":str(limit),"sortBy":"listDate",
        "order":"desc","offset":str(offset)
        }
    return _get_response(url, querystring)


def get_listings_near(near="Mesa", limit=100, offset=0):
    url = "https://rets.io/api/v1/armls/listings"
    querystring = {
        "access_token":"09d66e16b29cdd623dd1e7d0d0f1f062",
        "state[in][0]":"AZ","limit":str(limit),"sortBy":"listDate",
        "order":"desc","offset":str(offset),"near":near
        }
    return _get_response(url, querystring)


def batch_listings_near(near="Mesa"):
    mesa_list = []
    df = pd.DataFrame(json.loads(get_listings_near(offset=0))['bundle'])
    mesa_list.append(df)

    counter = 0
    while len(df) > 0:
        counter = counter + 1
        print('Running job {}, last job had {} listings'.format(counter, len(df)))
        df = pd.DataFrame(json.loads(get_listings_near(offset=100*counter))['bundle'])
        mesa_list.append(df)

    return mesa_list


def batch_arizona_listings():
    az_list = []
    df = pd.DataFrame(json.loads(get_arizona_listings(offset=0))['bundle'])
    az_list.append(df)

    counter = 0
    while len(df) > 0 and counter < 5:
        counter = counter + 1
        print('Running job {}, last job had {} listings'.format(counter, len(df)))
        df = pd.DataFrame(json.loads(get_arizona_listings(offset=100*counter))['bundle'])
        az_list.append(df)

    return az_list


if __name__=='__main__':
    print(get_approved_venders())
