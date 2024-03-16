import requests, time, delSymbol,sepet,os

def tbot(BOT_TOKEN,BOT_ID,Price,Coin,side,CoinList,TP,stpLoss):
    print("bot mesajı çalıstı")
    Time = time.strftime('%c')
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={BOT_ID}data=&text="+"Coin: "+ str(Coin) + "\n" + "Price: " + str(Price) + "\n" + "Side: "+ str(side) + "\n" + "TP: " + str(TP) + "\n" + "StopLoss: " + str(stpLoss) + "\n" + str(Time) )
    sepet.coinSepet(Coin,Price,TP,stpLoss,side)
    delSymbol.delSymbolList(Coin,CoinList)
    os.remove(f"1H_{Coin}.csv")