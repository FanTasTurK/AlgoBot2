import os,strategy,talib,config

BOT_TOKEN = config.BOT_TOKEN
BOT_ID = config.BOT_ID

def calculate(Coin,Price,Close,Hıgh,Low,secUp,secDown,CoinList):

    def calculateRSI(Coin,Close):
        try:
            global RSI
            FullRSI = talib.RSI(Close, timeperiod=14)   # RSI Hesaplama
            lenRSI = (len(FullRSI))                     # RSI Sayısını Bulma
            lastRSI = lenRSI - 1                        # RSI Sayısından 1 Çıkararak Son RSI İndeksi Hesaplama
            RSI = ((FullRSI[lastRSI]))                  # Güncel RSI Değeri
            RSI = round(RSI,2)
        except:
            os.remove(f"1H_{Coin}.csv")
            print("RSI HESAPLAMA HATASI")

    def calculateATR(Hıgh,Low,Close):
        global ATR
        FullATR = talib.ATR(Hıgh,Low,Close,timeperiod=30) # Stop Loss Hesaplama - ATR Hesaplama
        lenATR = (len(FullATR))                           # ATR Sayısını Bulma
        lastATR = lenATR - 1                              # ATR İndex Bulma
        ATR = ((FullATR[lastATR]))  
        ATR = round(ATR,2)                      # Güncel ATR Değeri

    def calculateADX(Hıgh,Low,Close):
        global ADX
        global DP
        global DN
        global DP2
        global DN2
        FullADX = talib.ADX(Hıgh,Low,Close,timeperiod=14) # Trend Gücü Ölçme - ADX Hesaplama
        lenADX = (len(FullADX))                           # ADX Sayısını Bulma
        lastADX = lenADX - 1                              # ADX İndex Bulma
        ADX = ((FullADX[lastADX]))                        # Güncel ADX Değeri
        ADX = round(ADX,2)
        DMIP = talib.PLUS_DI(Hıgh,Low,Close,timeperiod=30)
        DMIN = talib.MINUS_DI(Hıgh,Low,Close,timeperiod=30)
        DP = DMIP[-1]
        DP = round(DP,2)
        DP2 = DMIP[-2]
        DP2 = round(DP2,2)
        DN = DMIN[-1]
        DN = round(DN,2)
        DN2 = DMIN[-2]
        DN2 = round(DN2,2)

    def donc(Price,Coin,secUp,secDown,DP,DN,ADX,DP2,DN2,ATR):
        global side
        side = ""
        if Price > secUp and ADX >= 25 and DP > DN and DP2 < DN2 :
            side = "Long"
            TP = Price + 2*(ATR)
            stpLoss = Price - ATR
            strategy.strategy(Price,Coin,side,CoinList,TP,stpLoss,BOT_TOKEN,BOT_ID)
        elif Price < secDown and ADX >= 25 and DN > DP and DN2 < DP2 :
            side = "Short"
            TP = Price - 2*(ATR)
            stpLoss = Price + ATR
            strategy.strategy(Price,Coin,side,CoinList,TP,stpLoss,BOT_TOKEN,BOT_ID)

    calculateRSI(Coin,Close)
    calculateATR(Hıgh,Low,Close)
    calculateADX(Hıgh,Low,Close)
    donc(Price,Coin,secUp,secDown,DP,DN,ADX,DP2,DN2,ATR)
    print(f"Coin: {Coin} Price: {Price} RSI: {RSI} ADX: {ADX} DMI+: {DP} - {DP2} DMI-: {DN} - {DN2}")
    
