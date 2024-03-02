import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import random

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Locations''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Restore the data
with open('backup.data', 'r') as first, open('where.data', 'w') as second:
    for line in first:
        second.write(line)

# Randomly append a new university into current list
sf = open("random.data", 'r')
fh = open("where.data", 'a')

n = sum([1 for line in sf])
seed = random.randint(0, n-1)
sf.close()
sf = open("random.data", 'r')
for idx, line in enumerate(sf):
    if seed == idx:
        print('Automatic choose:\033[92m', line.rstrip(), '\033[00m')
        fh.write(line)
        break
sf.close()
fh.close()
time.sleep(3)

fh = open("where.data")
# count = 0
nofound = 0
for line in fh:
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database", address)
        continue
    except:
        pass

    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print("Retrieved {}, characters. The first 20 chars: '{}'".format(len(data), data[0:20].replace('\n', ' ')))
    # count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        nofound = nofound + 1

    cur.execute('''INSERT INTO Locations (address, geodata)
                VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    
fh.close()

if nofound > 0:
    print('Number of features for which the location could not be found:', nofound)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")

input()