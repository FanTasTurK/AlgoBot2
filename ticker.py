from binance.client import Client
from numpy import genfromtxt
import time, csv, calculate

def delSymbolList(Coin):
    CoinList.remove(Coin)

def tickers(API_KEY,API_SECRET,gecmisTarih):
    client = Client(API_KEY,API_SECRET)
    ticker = client.get_all_isolated_margin_symbols()

    global CoinList
    CoinList = []

    for i in ticker:
        if i["quote"] == "USDT":
            CoinList.append(i["symbol"])
    
    while True:
        for Coin in CoinList:
            csvfile = open(f'1H_{Coin}.csv', 'w', newline='')       # Coin Değişkeni ile Gelen Verileri Yazmak İçin csv Dosyası Oluşturmak
            candlestick_writer = csv.writer(csvfile, delimiter=',') # Gelen Verileri "," İşareti ile Bölmek 
            candlesticks = client.get_historical_klines((str(Coin)), Client.KLINE_INTERVAL_1HOUR, f"{gecmisTarih}" , "23 MAR, 2050") # Son Veriden İtibaren 14 Günlük Veriyi Çekmek

            for candlestick in  candlesticks:
                candlestick[0] = candlestick[0] / 1000
                candlestick_writer.writerow(candlestick)

            csvfile.close()
            try:
                global previousPrice

                data = genfromtxt(f"1H_{Coin}.csv" , delimiter=",")
                Close = data[:,4]                         # Tabloda 4. Sutun Kapanış Değerlerini Verir Mum Kapanmadıysa Güncel Fiyatı Gösterir
                LenClose = (len(Close))                   # Kapanış Değerlerinin Uzunluğunu Bulur
                lastClose = LenClose - 1                  # Güncel Fiyatın İndexini Bulmak
                Price = (Close[lastClose])               # Güncel Fiyat
                Hıgh = data[:,-10]                        # Bütün Yüksek Değerler Sutunu
                Low = data[:,-9]                          # Bütün Düşük Değerler Sutunu
                PreviousClose = LenClose - 2              # Bir Önceki Mum Kapanışının Sutun İndexi
                PreviousPrice = (Close[PreviousClose])   # Bir Önceki Mum Kapanışının Sutunu
                lenData = len(data)                       # Data Değişkeninin Uzunluğunu Bulmak
                lenData = lenData - 2                     # Data Değişkeninde Bir Önceki Satırı Hesaplamak
                previousPrice = data[lenData]             
                previousPrice = previousPrice[-8]         # Önceki Kapanış
                up = data[-30:,-10]
                down = data[-30:,-9]
                upMax = up.max()
                Up = up.argsort()
                secUp = Up[-2]
                secUp = up[secUp]
                downMin = down.min()
                Down = down.argsort()
                secDown = Down[1]
                secDown = down[secDown]
                calculate.calculate(Coin,Price,Close,Hıgh,Low,secUp,secDown,CoinList)
            except:
                pass

        print("Finish")
        time.sleep(600)