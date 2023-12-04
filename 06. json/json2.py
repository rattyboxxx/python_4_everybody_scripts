import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter link: ')
    if len(address) < 1: break
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()
    info = json.loads(data)['comments']
    sum = 0
    for item in info:
        sum += int(item['count'])
    print(sum)
    break
