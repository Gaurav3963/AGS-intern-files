from django.views.generic import TemplateView
from django.shortcuts import render
from .processtable import process_table, display_table

def index(request):
    if request.method == "POST":
        file1 = request.FILES['document']
        a = process_table(file1)
    return render(request,'index.html')

def tableview(request):
    var = display_table("tabledata")
    return render(request,'displaytable.html',{'table':var,'Name':"tabledata"})