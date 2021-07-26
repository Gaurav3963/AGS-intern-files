from django.shortcuts import render
from Transactions import models
from .models import FileUpload
from Transactions import logic
from datetime import datetime

def index(request):
    options = ['Date','Time','Type','TypeDesc','MsgType','CardNo','FromAccount','TerminalID','TraceNo','TransactionID','STAN','AmountReq','AmountRsp','CurrencyCode','IntlAmountReq','IntlAmountRsp','ResponseCode','ResponseDesc','AuthIDRsp','ExtTranType','ExtTranTypeDesc','MerchantType','MerchantTypeCode','MerchantTypeDesc','MerchantID','MerchantLocation','AcquiringBin','CardProduct','Source','Location','Node','retention_data','icc_data_req','acquiring_inst_id_code','pos_entry_mode','pos_condition_code','additional_rsp_data','ucaf_data','card_verification_result','pos_geographic_data','cvv_available_at_auth','cvv2_available_at_auth','Mask Card No','card_seq_nr','expiry_date','service_restriction_code','address_verification_data','address_verification_result','pos_card_data_input_ability','pos_cardholder_auth_ability','pos_card_capture_ability','pos_operating_environment','pos_cardholder_present','pos_card_present','pos_card_data_input_mode','pos_cardholder_auth_method','pos_cardholder_auth_entity','pos_card_data_output_ability','pos_terminal_output_ability','pos_pin_capture_ability','pos_terminal_operator','pos_terminal_type','secure_3d_result','pos_data']
    column = ['Date','Time','CardNo','FromAccount','TerminalID','TransactionID','MerchantID']
    s = options.copy()
    for i in column:
        s.remove(i)
    defi = {}
    positions = list(range(1,len(s)))
    for i in s:
        for j in positions:
            defi[i]=j
            positions.remove(j)
            break
    print(defi)
    if request.method == "POST":
        
        try:
            data = ""
            Error = ""

            try :
                status = request.POST['tname']

                # Parameter to Find Data

                if(status=="tranTransactionID"):
                    try :
                        value = request.POST['transactionIID']
                        data = models.TransactionDetails.objects.filter(tranTransactionID=value)
                    except :
                        return render(request,'index.html',{'data':data,'table':True,'Error':"Transaction ID Is Wrong or Not Given"})

                elif(status == "tranTerminalID"):
                    try :
                        value=request.POST['terminalID']
                        data = models.TransactionDetails.objects.filter(tranTerminalID=value)
                    except :
                        return render(request,'index.html',{'data':data,'table':True,'Error':"Terminal ID Is Wrong or Not Given"})

                elif(status == "tranDate"):
                    try :
                        value=request.POST['date']
                        print(value)
                        value = datetime.strptime(value, '%d-%m-%Y').date()
                        print(value)
                        data = models.TransactionDetails.objects.filter(tranDate=value)
                    except :
                        return render(request,'index.html',{'data':data,'table':True,'Error':"Terminal ID Is Wrong or Not Given"})

            except : 
                return render(request,'index.html',{'data':data,'table':True,'Error':"Pls mark your Choice"})

            choice = ""

            # Options to display Row

            for i in options :
                try:
                    if choice=="":
                        choice = choice + request.POST[i]
                    else:
                        choice = choice + "|"+ request.POST[i]
                except: 
                    choice = choice
            # Checking If Any Data is Available or not 

            if data.count()==0:
                Error = "No Data Found"
                return render(request,'index.html',{'table':False,'error':Error})
            
            # Sending Data to templates

            choice = choice.split('|')
            data_list = list(data.values()) 
            new_list = []
            choiceValue = {}

            for i in data_list:
                print(choice)
                for j in choice:
                    index = defi.get(j,0)
                    index = int(index)
                    if index == 0:
                        try :
                            a = "tran"+j
                            choiceValue[j]=i[a]
                        except:
                            break
                    else :
                        choiceValue[j] = i['transData'].split('|')[index]
                
                MainDetails = {
                       "TransactionID": i['tranTransactionID']
                    }
                MainDetails.update(choiceValue)
                new_list.append(MainDetails)
            print(new_list)
            return render(request,'index.html',{'data':new_list,'option':choice,'table':True,'Error':"Data Found",'options':options})
        
        except Exception as e:
            print("Error Occured"+e)
            
    return render(request,'index.html',{'table':False,'options':options}) 

def upload(request):
    context = {
        'status':"Not Uploaded"
    }
    if request.method == "POST":
        #file1 = request.FILES['myfile']
        #document = FileUpload.objects.create(file = file1)
        #document.save()
        logic.executefile("")
        return render(request,'index.html',{'status':"Uploaded"})
    return render(request,'upload.html',context)