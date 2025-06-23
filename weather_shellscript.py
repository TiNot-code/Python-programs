import time
import openmeteo_requests

import pandas as pd
import requests_cache
import json
from pprint import pprint

from retry_requests import retry


# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2) 
openmeteo = openmeteo_requests.Client(session = retry_session)

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 51.3396,
	"longitude": 12.3713,
	"current": ["temperature_2m", "precipitation"],
	"forecast_days": 2
}

def truncate(f, n) -> str:
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]

# Current values. The order of variables needs to be the same as requested.
current = response.Current()
current_temp = truncate(current.Variables(0).Value(),1) + "°C"
current_precipitation = current.Variables(1).Value()

# Get the timestamp and convert it into date/time -> seperate by space
ct = time.ctime(time.time())
ct = ct.split()

# Print the vars
print(f"Hello, user :)")
print(f"Time: {ct[3]} on the {ct[2]} { ct[1]} of",ct[4])
print(f"Current Temperature in Leipzig {current_temp}")
print(f"Current precipitation {current_precipitation} %")
