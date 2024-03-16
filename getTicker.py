import config,getDate
from binance.client import Client

API_KEY = config.API_KEY
API_SECRET = config.API_SECRET

def getSymbols(API_KEY,API_SECRET):
    client = Client(API_KEY,API_SECRET)
    ticker = client.get_all_isolated_margin_symbols()

    global CoinList
    CoinList = []

    for i in ticker:
        if i["quote"] == "USDT":
            CoinList.append(i["symbol"])

getSymbols(API_KEY,API_SECRET)

getDate()