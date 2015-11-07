import requests


headers = {
    'cache-control': "no-cache",
    }


def get_approved_venders():
    url = "https://rets.io/api/v1/vendors/approved"

    querystring = {"access_token":"09d66e16b29cdd623dd1e7d0d0f1f062"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


def get_arizona_transactions():
    url = "https://rets.io/api/v1/armls/transactions"

    querystring = {"access_token":"09d66e16b29cdd623dd1e7d0d0f1f062"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


def get_arizona_listings():
    url = "https://rets.io/api/v1/armls/listings"

    querystring = {"access_token":"09d66e16b29cdd623dd1e7d0d0f1f062","state[in][0]":"AZ","limit":"50"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


if __name__=='__main__':
    print(get_approved_venders())
