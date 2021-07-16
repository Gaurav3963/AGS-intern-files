from django.shortcuts import render
from Transactions import models

def index(request):
    #data = models.TransactionDetails.objects.all()
    if request.method == "POST":
        print("\n\n\n-----------------------------------------------------------------------\n")
        print("POST request posted with option : "+request.POST['details'])
        print("\n-------------------------------------------------------------------\n\n\n")
        status = request.POST['tname']
        data = ""
        Error = ""
        if(status=="tranTransactionID"):
            value = request.POST['transactionIID']
            data = models.TransactionDetails.objects.filter(tranTransactionID=value)
            print(value)
        elif(status == "tranTerminalID"):
            value=request.POST['terminalID']
            print(value)
            data = models.TransactionDetails.objects.filter(tranTerminalID=value)
            if data.count()==0:
                Error = "No Data Found"
                return render(request,'index.html',{'table':False,'error':Error})
        return render(request,'index.html',{'data':data,'table':True,'error':"Data Found"})
    return render(request,'index.html',{'table':False}) 