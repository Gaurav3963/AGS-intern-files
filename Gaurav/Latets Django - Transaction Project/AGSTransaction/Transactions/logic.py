from AGSTransaction.settings import MEDIA_ROOT
from Transactions.models import TransactionDetails
import pandas as pd
from Transactions import models
from datetime import datetime

def getData(data,index):
    data = data.split("|")
    return data[index]


def choose(value,columnName,models):
    try :
        data = models.TransactionDetails.objects.filter(columnName=value)
    except :
        return 0

def executefile(file):
    file = str(MEDIA_ROOT)+str(file)
    data = pd.read_csv(file)
    data = data.to_dict("records")
    #print(data)
    for row in data:
        a = row
        date = a['TranDate']
        date = datetime.strptime(date, '%d-%m-%Y').date()
        del a['TranDate']
        time = a['TranTime']
        time = datetime.strptime(time, '%H:%M:%S').time()
        del a['TranTime']
        cardNo = a['CardNo']
        cardNo = str(cardNo)
        del a['CardNo']
        fromAccount = a['FromAccount']
        fromAccount = str(fromAccount)
        del a['FromAccount']
        terminalID = a['TerminalID']
        terminalID = str(terminalID)
        del a['TerminalID']
        transactionID = a['TransactionID']
        transactionID = str(transactionID)
        del a['TransactionID']      
        merchantID = a['MerchantID']
        merchantID = str(merchantID)
        del a['MerchantID']
        TransData = ""
        for column in a :
            TransData = TransData + str(row[column]) +"|"
        print("______________________________________")
        #print(TransData)
        b = TransactionDetails(tranDate = date,tranTime = time,tranCardNo = cardNo,tranFromAccount = fromAccount,tranTerminalID = terminalID,tranTransactionID = transactionID,tranMerchantID = merchantID,transData = TransData)
        return b 
#executefile("a")