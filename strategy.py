import bot

def strategy(Price,Coin,side,CoinList,TP,stpLoss,BOT_TOKEN,BOT_ID):
    bot.tbot(BOT_TOKEN,BOT_ID,Price,Coin,side,CoinList,TP,stpLoss)