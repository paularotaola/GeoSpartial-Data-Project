import requests
from dotenv import load_dotenv
load_dotenv()
import googlemaps
import os


def geocode(address):
    """
    Saca las coordenadas de una dirección que le des.
    """
    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]}


def requestFoursquare(query,data,radio=1000):
    """
    Hace requests a la API de Foursquare en funcion de un query específico y un radio
    """
    client_idd = os.getenv("4S_CLIENT_ID")
    client_secret=os.getenv("CLIENT_SECRET")
    
    long = data['longitude']
    lat = data['latitude']

    params = {"client_id": client_idd,
              "client_secret":client_secret,
              "v": "20180323",
              "ll":f'{lat},{long}',
              "radius":f'{radio}',
              "query":f'{query}', 
              "limit":20 }

    url = f"https://api.foursquare.com/v2/venues/explore"
    
    resp = requests.get(url=url, params=params)
    res = json.loads(resp.text)

    return res["response"]["totalResults"]


def gPlaces (lat,long,query,rad=1000):
    """
    Hace requests a la API de Google en funcion de un query específico y un radio
    """
    apiKey = os.getenv('GPLACES_APIKEY')
    gmaps =googlemaps.Client(key=apiKey)
    
    places = gmaps.places_nearby(location=[lat,long], radius=rad,open_now=False, type=query)
    return places["results"]