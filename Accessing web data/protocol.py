import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        tree = json.loads(data)
    except:
        tree = None

    print(json.dumps(tree,indent=4))


    counts = len(tree["comments"])
    sum = 0
    for i in range(counts):
        sum += float(tree["comments"][i]["count"])
    print(sum)


    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text
    #print(location)
