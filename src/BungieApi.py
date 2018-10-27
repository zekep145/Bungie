# This class wraps all API calls we'll be playing with
import requests
import json

class BungieAPI:
    url = 'https://www.bungie.net/Platform'
    api_key = ''

    def __init__(self):
        print("Initializing API")

    def Authorize(self):
        print("Attempting to authorize with bungie.net")
        payload = {'some': 'data'}
        headers = {'X-API-Key': self.api_key}

        response = requests.get(self.url, headers = headers).json()
        with open('json_response.json', encoding='utf-8', mode='w') as file:
            file.write(json.dumps(response, indent=4, sort_keys=True))