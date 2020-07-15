#Trading algo test
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import os
import finnhub
import json
import requests
import quandl
import pandas as pd

load_dotenv()

APCA_API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
FINN_API_KEY = os.getenv("FINN_API_KEY")
Q_API_KEY = os.getenv("Q_API")
ALPHA_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

quandl.ApiConfig.api_key = Q_API_KEY

teny = quandl.get("USTREASURY/YIELD", start_date="2020-07-10", end_date="2020-07-10")
tips = quandl.get("USTREASURY/REALYIELD", start_date="2020-07-10", end_date="2020-07-10")
spxeps = quandl.get("MULTPL/SP500_EARNINGS_MONTH")
teny = teny["10 YR"].values[0]
tips = tips["10 YR"].values[0]
spxeps = spxeps["Value"].tail(1).values[0]

# Configure API key
configuration = finnhub.Configuration(
    api_key={
        'token':FINN_API_KEY
    }
)

finnhub_client = finnhub.DefaultApi(finnhub.ApiClient(configuration))

r = requests.get(f'https://finnhub.io/api/v1/stock/metric?symbol=HD&metric=price&token={FINN_API_KEY}')
beta = r.json()
beta = beta["metric"]["beta"]

div = requests.get("https://api.unibit.ai/v2/company/actions/dividends/?tickers=HD&startDate=2019-01-01&endDate=2020-07-07&dataType=json&accessKey=Hkk9fY74xhwxx9ODNhm7OqdSAN7a8gbc")
div = div.json()
div = div["result_data"]

divt = div[0]["dividend"]
divly = div[3]["dividend"]

dgr = (divt - divly)/divly * 100

if dgr < 2.0:
    dgr = 2.0
    period = "stable"
    print(dgr)
else:
    diff = (dgr - 2.0)/5
    dgr1 = (dgr - diff)
    dgr2 = (dgr1 - diff)
    dgr3 = (dgr2 - diff)
    dgr4 = (dgr3 - diff)
    dgr5 = (dgr4 - diff)
    period = "growth"


# for x in range(len(div)):
#     print(div[x]["dividend"])

url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=SPY&apikey={ALPHA_API_KEY}"
response = requests.get(url)
raw_data = json.loads(response.text)
spx = float(raw_data["Global Quote"]["05. price"])*10
expr = spxeps/spx*100
erp = expr - teny

coe = (teny + beta * erp)/100

if period == "stable":
    value = "nothing"
else:
    div1 = divt * (1+dgr1/100)
    div2 = div1 * (1+dgr2/100)
    div3 = div2 * (1+dgr3/100)
    div4 = div3 * (1+dgr4/100)
    div5 = div4 * (1+dgr5/100)
    pv1 = div1/(1+coe)
    pv2 = div2/(1+coe)**2
    pv3 = div3/(1+coe)**3
    pv4 = div4/(1+coe)**4
    pv5 = div5/(1+coe)**5
    pvt = ((div5 * 1.02)/(coe - 0.02))/(1+coe)**5
    value = (pv1 + pv2 + pv3 + pv4 + pv5 + pvt)

print(value)

api = tradeapi.REST(APCA_API_KEY, API_SECRET_KEY, api_version='v2')
# account = api.get_account()
# value = api.get_last_quote("SPY")
# orders = api.list_orders()
# positions = api.list_positions()

# api.submit_order(
#     symbol='F',
#     side='buy',
#     type='market',
#     qty='100',
#     time_in_force='day',
# )

# print(account)
# print(account.status)
# print(type(value))
# print(orders)
# print(positions)

# Quote
# print(finnhub_client.quote('AAPL'))

# # Basic financials
# price = json.loads(finnhub_client.company_basic_financials('AAPL', 'price'))
# print(price)