import uuid
from pprint import pprint
import os
from dotenv import load_dotenv
import requests

load_dotenv()



KALSHI_HOST = os.getenv('KALSHI_HOST')
KALSHI_USERNAME = os.getenv('KALSHI_USERNAME')
KASLHI_PASSWORD = os.getenv('KASLHI_PASSWORD')

url = KALSHI_HOST + '/login'
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}
body = {
    "email": KALSHI_USERNAME,
    "password": KASLHI_PASSWORD
}
response = requests.post(url, headers=headers, json=body)
token = response.json()['token']

url = "https://trading-api.kalshi.com/trade-api/v2/markets/INXU-24FEB28-T5074.99/history"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + token
}
response = requests.get(url, headers=headers)
pprint(response.json())
