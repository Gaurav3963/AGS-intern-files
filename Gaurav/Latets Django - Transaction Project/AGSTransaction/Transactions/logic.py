from AGSTransaction.settings import MEDIA_ROOT
import pandas as pd
from Transactions import models

def getData(data,index):
    data = data.split("|")
    return data[index]


def choose(value,columnName,models):
    try :
        data = models.TransactionDetails.objects.filter(columnName=value)
    except :
        return 0

def executefile(file):
    #file = str(MEDIA_ROOT)+str(file)
    file = "C:\Office\AGS - Internship\AGS-intern-files\Gaurav\Latets Django - Transaction Project\s.csv"
    data = pd.read_csv(file)
    data = data.to_dict("records")
    #print(data)
    for row in data:
        a = row
        date = a['TranDate']
        del a['TranDate']
        time = a['TranTime']
        del a['TranTime']
        cardNo = a['CardNo']
        del a['CardNo']
        fromAccount = a['FromAccount']
        del a['FromAccount']
        terminalID = a['TerminalID']
        del a['TerminalID']
        transactionID = a['TransactionID']
        del a['TransactionID']      
        merchantID = a['MerchantID']
        del a['MerchantID']
        TransData = ""
        for column in a :
            TransData = TransData + str(row[column]) +"|"
        print("______________________________________")
        print(TransData)
        b = models.TransactionDetails( 
            tranDate = date,
            tranTime = time,
            tranCardNo = cardNo,
            tranFromAccount = fromAccount,
            tranTerminalID = terminalID,
            tranTransactionID = transactionID,
            tranMerchantID = merchantID,
            transData = TransData)
        b.save()
    
#executefile("a")