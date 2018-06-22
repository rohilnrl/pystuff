import xml.etree.ElementTree as ET
import urllib.request, urllib.error, urllib.parse
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)

s = 0
for tag in tree[1]:
    s += int(tag[1].text)

print(s)