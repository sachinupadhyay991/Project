from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import *
def index(request):
    ob1 = Global_Indices.objects.all()[:5]
    ob2 = MAS_BSE.objects.all()[:5]
    ob3 = MAS_NSE.objects.all()[:5]
    ob4 = FD_CASH.objects.all()[:3]
    ob5 = FD_FII.objects.all()[:3]
    ob6 = Indian_Indices.objects.all()[:5]
    labels = []
    data = []

    queryset = graph.objects.all()
    for i in queryset:
        labels.append(i.year)
        data.append(i.price)
    


    d = {'tb1': ob1,'tb2': ob2,'tb3': ob3,'tb4': ob4,'tb5': ob5,'tb6':ob6,'year':labels,'price':data}
    return render(request, 'home.html',context=d)


def viewmore(request,id):
    obj1 = Global_Indices.objects.all()
    obj2 = Indian_Indices.objects.all()
    obj3 = MAS_BSE.objects.all()
    obj4 = MAS_NSE.objects.all()
    obj5 = FD_CASH.objects.all()
    obj6 = FD_FII.objects.all()
    

    if id==1:
        heading = 'Global Indices'
        header = ['Name','Current Value','Change','% Chg','Open','High','Low','Prev Close']
        rows = []
        for i in obj1:
            rows.append([i.Name,i.Currrent_value,i.change,i.Per_change,i.Open,i.High,i.Low,i.pre_close])
    elif id==2:
        heading = 'Indian_Indices'
        header = ['Name','Current Value','Change','% Chg','Open','High','Low']
        rows = []
        for i in obj2:
            rows.append([i.Name,i.Currrent_value,i.change,i.Per_change,i.Open,i.High,i.Low])
    elif id==3:
        heading = 'MOST ACTIVE STOCKS BSE'
        header = ['Company Name','Group','High','Low','Last Price','% Change','Values (Rs. cr.)']
        rows = []
        for i in obj3:
            rows.append([i.Company_name,i.Group,i.High,i.Low,i.Last_Price,i.Per_change,i.Values_in_RS])
    elif id==4:
        heading = 'MOST ACTIVE STOCKS NSE'
        header =['Company Name','High','Low','Last Price','% Change','Values (Rs. cr.)']
        rows = []
        for i in obj4:
            rows.append([i.Company_name,i.High,i.Low,i.Last_Price,i.Per_change,i.Values_in_RS])
    elif id==5:
        heading = "FII & DII TRADING ACTIVITY DURING MAY '20"
        header = ['Date','Gross Purchase','Gross Sales','Net Purchase / Sales','Gross Purchase','Gross Sales','Net Purchase / Sales']
        rows = []
        for i in obj5:
            rows.append([i.F_date,i.F_gross_purchase,i.F_gross_sales,i.F_net_purchase_orsale,i.D_gross_purchase,i.D_gross_sales,i.D_net_purchase_orsale])
    elif id==6:
        heading = "FII & DII TRADING ACTIVITY DURING MAY '20"
        header = ['Date','Gross Purchase','Gross Sales','Net Purchase / Sales','Gross Purchase','Gross Sales','Net Purchase / Sales']
        rows = []
        for i in obj6:
            rows.append([i.E_date,i.E_gross_purchase,i.E_gross_sales,i.E_net_purchase_orsale,i.DE_gross_purchase,i.DE_gross_sales,i.DE_net_purchase_orsale])
    
    
    return render(request,"Viewmore.html",{'heading':heading,'header':header,'rows':rows})