
import requests


def get_lat_lng(raw_address):
    address = raw_address
    payload = {
        'address': address,
        'benchmark': 4,
        'format': 'json'
    }
    r = requests.get('https://geocoding.geo.census.gov/geocoder/locations/onelineaddress', params=payload)

    return r.json()