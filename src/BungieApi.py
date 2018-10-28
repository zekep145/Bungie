# This class wraps all API calls we'll be playing with
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


class BungieAPI:
    base_url = 'https://www.bungie.net/Platform/Destiny2/'
    xur_url = base_url + 'Destiny/Advisors/Xur'
    api_key = os.environ['API_KEY']
    headers = {'X-API-Key': api_key}

    def __init__(self):
        print("Initializing API")

    def get_userid(self, user):

        print(user)

    def get_characters(self, user_id):
        print("Checking for characters for ID: {0}".format(user_id))

        response = requests.get(self.base_url + '4/Profile/{0}?components=Characters'.format(user_id), headers=self.headers).json()

        for character in response['Response']['characters']['data']:
            print(character)

        print(json.dumps(response, indent=4, sort_keys=True))
