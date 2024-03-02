import urllib.request, urllib.parse, urllib.error
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter link: ')
    if len(address) < 1: break
    uh = urllib.request.urlopen(address, context=ctx)
    data = str(uh.read())
    sum = 0
    lst = re.findall("[0-9]+", data)
    for i in lst:
        sum += int(i)
    print(sum)
    break
