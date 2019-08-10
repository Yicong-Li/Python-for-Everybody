import urllib.request, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
info = json.loads(data)
Count = 0
Sum = 0
for item in info['comments']:
    Sum = Sum + item['count']
    Count = Count + 1
print('Count:', Count)
print('Sum:', Sum)
