import json
import urllib.request
import urllib.parse
import urllib.error

# Retrieving http://
serviceurl = "http://py4e-data.dr-chuck.net/json?"

# address
address = input('Enter location: ')
url = serviceurl + urllib.parse.urlencode(
    {'key': 42,  'address': address})

# print("Enter location:", address)

print('Retrieving', url)

uh = urllib.request.urlopen(url)

data = uh.read()


info = json.loads(data)
print('Retrieved', len(data), 'characters')

# print place id
print("Place id " + info['results'][0]['place_id'])
