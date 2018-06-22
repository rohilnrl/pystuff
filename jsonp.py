import json
import re
import requests
import ssl
import urllib.parse as parse

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/geojson?' + parse.urlencode({'address':'Transilvania University'})
url = requests.get(url)

js = json.loads(url.text)

print(js['results'][0]['place_id'])