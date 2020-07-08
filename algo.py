#Trading algo test

import alpaca_trade_api as tradeapi

api = tradeapi.REST('<key_id>', '<secret_key>', api_version='v2') # or use ENV Vars shown below
account = api.get_account()

print(account)