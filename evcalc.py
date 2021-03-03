#Calculate EV Ratios
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import os
import requests

load_dotenv()

APCA_API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("BASE_URL")
IEXAPI = os.getenv("IEX_API_KEY")

symbol = input("Enter Stock Symbol: ") 
api = tradeapi.REST(APCA_API_KEY, API_SECRET_KEY, BASE_URL)
price = api.get_last_trade("AAPL")
r = requests.get(f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={IEXAPI}')
mc = r.json()['marketCap']
r = requests.get(f'https://cloud.iexapis.com/stable/stock/{symbol}/balance-sheet?token={IEXAPI}')
y = r.json()
cash = y['balancesheet'][0]['currentCash']
std = y['balancesheet'][0]['currentLongTermDebt']
ltd = y['balancesheet'][0]['longTermDebt']
ev = mc + std + ltd - cash
r = requests.get(f'https://cloud.iexapis.com/stable/stock/{symbol}/income?period=annual&token={IEXAPI}')
rev = r.json()['income'][0]['totalRevenue']
ebit = r.json()['income'][0]['ebit']
print(f'EV/Sales: {ev/rev}')
print(f'EV/EBIT: {ev/ebit}')
