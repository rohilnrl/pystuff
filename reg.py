from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input('Enter count: ')) - 1
pos = int(input('Enter positon: ')) - 1

for i in range(count):
    url = soup('a')[pos]['href']
    print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')


# print(re.findall('by_(.*)\.', soup('a')[2]['href'])[0])
print(soup('a')[pos]['href'])