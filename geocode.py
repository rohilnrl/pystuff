#! python3

# Retrieves address coordinates.

import json
import re
import requests
import ssl
import urllib.parse as parse

print('CTRL+C to exit.\n')

def reset_params():
    parameters = {'address': ''}

    service_url = 'https://maps.googleapis.com/maps/api/geocode/'
    url = service_url

def get_status(status):
    if status == 'OK':
        print('Data retrieved.')
    elif status == 'OVER_QUERY_LIMIT':
        print('Daily API request limit exceeded.\nTry again tomorrow.')


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parameters = {'address': ''}

service_url = 'https://maps.googleapis.com/maps/api/geocode/'
url = service_url

while True:

    try:
        form = input('Enter format: ')
    except:
        break

    if len(form) < 1:
        print('Invalid format.')
        reset_params()
        continue

    url += form

    address = input('Enter address: ')

    if len(address) < 1:
        print('Invalid address.')
        reset_params()
        continue

    parameters['address'] = parse.urlencode({'':address})[1:]

    data = requests.get(url, params=parameters).text

    try:
        js = json.loads(data)
    except:
        print('Data retrieved was not in correct format.')
        break
    
    if js['status'] == 'OVER_QUERY_LIMIT':
        print('Daily API request limit exceeded.\nTry again tomorrow.')
        break

