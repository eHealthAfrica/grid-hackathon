import requests

url = "https://api.grid-nigeria.org/"

def datasets(resource_name, size=200, page=1, sort_by="global_id", fields=""):
    endpoint = "{}{}".format(url, resource_name)
    querystring = {"size":size,"page":page,"sort_by":sort_by,"fields":fields}
    response = requests.request("GET", endpoint, params=querystring)
    return response.text
    