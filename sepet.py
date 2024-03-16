import csv

def coinSepet(Coin,Price,TP,stpLoss,side):
    csvfile = open("1111Sepet.csv","a",newline="")
    yaz = csv.writer(csvfile, delimiter=",")
    data = Coin, Price, TP, stpLoss, side
    yaz.writerow(data)
    csvfile.close()