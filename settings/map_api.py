import os

import googlemaps

GOOGLE_MAP_API_KEY = os.getenv('GOOGLE_MAP_API_KEY')

GMAPS = googlemaps.Client(key=GOOGLE_MAP_API_KEY)
