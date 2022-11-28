import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit('Ism kiritmading.')

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" 
+ sys.argv[1])

# print(json.dumps(response.json(), indent=2))
o = response.json()['results']

for result in o:
    print(result['trackName'])