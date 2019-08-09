import urllib.request, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
results = tree.findall('.//count')
count = 0
Sum = 0
for result in results:
    count = count + 1
    number = int(result.text)
    Sum = Sum + number
print('Count:', count)
print('Sum:', Sum)
