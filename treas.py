#Calculate EV Ratios
from dotenv import load_dotenv
import os
import requests

load_dotenv()

IEXAPI = os.getenv("IEX_API_KEY")

#r = requests.get(f'https://cloud.iexapis.com/stable/time-series/treasury/DGS20?from=2021-01-01&to=2021-03-01&token={IEXAPI}')
thirty = requests.get(f'https://cloud.iexapis.com/stable/data-points/market/DGS30?token={IEXAPI}').json()
five = requests.get(f'https://cloud.iexapis.com/stable/data-points/market/DGS5?token={IEXAPI}').json()
print(thirty-five)