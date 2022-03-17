""" Maps uses maps.py to create a map to display a circle at each region's geographic center with the diameter corresponding to the number of records in that region """

import pandas as pd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium

locator = Nominatim(user_agent="myGeocoder")
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

coords = []
coords.append(locator.geocode("North East England"))
coords.append(locator.geocode("North West England"))
coords.append(locator.geocode("Yorkshire and Humber"))
coords.append(locator.geocode("East Midlands England"))
coords.append(locator.geocode("West Midlands England"))
coords.append(locator.geocode("East of England"))
coords.append(locator.geocode("London"))
coords.append(locator.geocode("South East England"))
coords.append(locator.geocode("South West England"))
coords.append(locator.geocode("Wales"))

def generate_map(df, names):
    records_per_region = list(df.groupby(['Region']).Region.count())
    map = folium.Map(location=[54, -2.5], zoom_start=6)
    for x in range(len(coords)):
        folium.Circle(location=[coords[x].latitude, coords[x].longitude], 
        popup=names[x], 
        radius=records_per_region[x],
        color='blue',
        fill=True,
        fill_color='blue'
        ).add_to(map)
    return map
