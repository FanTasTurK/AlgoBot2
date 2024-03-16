import datetime,ticker,config

API_KEY = config.API_KEY
API_SECRET = config.API_SECRET

def date():
    datetime.datetime.today()
    bugün = datetime.datetime.today()

    fark = datetime.timedelta(days=35)
    geçmiş = bugün - fark
    geçmişAY = geçmiş.strftime("%b")
    geçmişGÜN = geçmiş.strftime("%d")
    geçmisYIL = geçmiş.strftime("%Y")
    global gecmisTarih
    gecmisTarih = (f"{geçmişGÜN} {geçmişAY} {geçmisYIL} ")
    ticker.tickers(API_KEY,API_SECRET,gecmisTarih)