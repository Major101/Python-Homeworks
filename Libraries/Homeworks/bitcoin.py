import sys
import requests
import json

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number.")
except IndexError:
    sys.exit('Missing command-line argument.')


try:
    response = requests.get(url)
except requests.RequestException:
    sys.exit('INTERNET YOGGGGGGGGGGGGGGGGGG!') 

price = response.json()['bpi']['USD']['rate_float']

# print(json.dumps(response.json(), indent=2))
print(f'${(price*number):,.4f}')