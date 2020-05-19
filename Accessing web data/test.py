# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
url = input('Enter - ')
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def link(url):

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    l =list()
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        z= tag.get('href', None)
        l.append(z)

    url = l[17]
    print(url)
    l.clear()
    link(url)
for i in range(4):
    link(url)
