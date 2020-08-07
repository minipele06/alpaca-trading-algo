#Trading algo test
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import os
import json

load_dotenv()

APCA_API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("BASE_URL")

# print(APCA_API_KEY)
# print(API_SECRET_KEY)

api = tradeapi.REST(APCA_API_KEY, API_SECRET_KEY, BASE_URL)
price = api.get_last_trade("AAPL")
data = api.get_aggs("AAPL","1","day","2020-06-06","2020-07-31")

print(price.price)
print(data)

