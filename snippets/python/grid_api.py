import requests

url = "https://api.grid-nigeria.org/"

def getDatasets(resource_name, size=200, page=1, sort_by="global_id", fields="", cql=""):
    endpoint = "{}{}".format(url, resource_name)
    querystring = {"size":size,"page":page,"sort_by":sort_by,"fields":fields, "cql":cql }
    response = requests.request("GET", endpoint, params=querystring)
    return response.url