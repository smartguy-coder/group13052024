import requests


API_KEY = 'TgfYYWui2hfp'
BASE_URL = 'https://api.unitalk.cloud/api'
DIRECT_PHONE_PATH = '/phones/directCall'
SIP = '5661'  # inner unitalk phone number

final_url = f'{BASE_URL}{DIRECT_PHONE_PATH}'

headers = {
    'Authorization': API_KEY,
}

data = {
    'sip': SIP,
    'number': '380919056490',
    'meta': ',bdfjdbv'
}

response = requests.post(final_url, headers=headers, data=data)


print(response.json())
