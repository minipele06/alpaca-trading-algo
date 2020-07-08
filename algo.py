#Trading algo test
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import os

load_dotenv()

API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")

api = tradeapi.REST(API_KEY, API_SECRET_KEY, api_version='v2') # or use ENV Vars shown below
account = api.get_account()

print(account.status)