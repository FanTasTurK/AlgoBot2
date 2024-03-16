import csv, config
from binance.client import Client
from ticker import *
import pandas as pd

API_KEY = config.API_KEY
API_SECRET = config.API_SECRET

def tpWatch():
    rows = []
    with open("1111Sepet.csv" ,newline="") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)
    file.close()
    exit = len(rows)

    df = pd.read_csv("1111Sepet.csv", delimiter=",")



    x = 0
    while True:
        sutun = rows[x]
        coin = sutun[0]
        tp = sutun[2]
        loss = sutun[3]
        side = sutun[4]
        print(coin,tp,loss,side)

        client = Client(API_KEY,API_SECRET)
        ticker = client.get_symbol_ticker(symbol=coin)
        price = ticker["price"]

        if side == "Long" and price >= tp:
            print(f"{coin} TP Başarılı")
            df.drop([x])
            
        elif side == "Long" and price <= loss:
            print(f"{coin} Stop Oldu")
            df.drop([x])

        elif side == "Short" and price <= tp:
            print(f"{coin} TP Başarılı")
            df.drop([x])

        elif side == "Short" and price >= loss:
            print(f"{coin} Stop Oldu")
            df.drop([x])

        else:
            print(f"{coin} Poz Açık")
        
        x += 1
        
        if exit <= x:
            break

tpWatch()