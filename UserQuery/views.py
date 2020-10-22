from django.shortcuts import render
from django.http import HttpResponse
from .CallScript import call_script
import time
# Create your views here.

def look(request):
    context={}
    callType = '101'
    if request.method == 'POST':
        nbr = request.POST.get('number')
        #userType = request.POST.get('user_type')
        #print(nbr,userType) 
        #message=call_script('UserQuery',nbr,callType,userType)
        message = call_script('UserQuery', nbr, callType)
        if message:
            context={'message':message,'number':nbr}
            return render(request,'look/look.html',context)
        else:
            message = '脚本调用失败，请联系管理员！'
            context={'message':message,'number':nbr}
            return render(request,'look/look.html',context)
    return render(request,'look/look.html')

def pre_look(request):
    context = {}
    callType = '103'
    if request.method == 'POST':
        nbr=request.POST.get('number')
        #userType = request.POST.get('user_type')
        #print(nbr,userType)
        message = call_script('UserQuery',nbr,callType)
        if message:
            context={'message':message,'number':nbr}
            return render(request,'pre_look/pre_look.html',context)
        else:
            message = '脚本调用失败，请联系管理员！'
            context={'message':message,'number':nbr}
            return render(request,'pre_look/pre_look.html',context)
    return render(request,'pre_look/pre_look.html')

def zero_balance(request):
    context={}
    callType = '110'
    if request.method=='POST':
        nbr=request.POST.get('number')
        datetime=request.POST.get('user_date').replace('-','')
        #userType=request.POST.get('user_type')
        message=call_script('UserQuery',nbr,callType,datetime)
        if message:
            context={'message':message,'number':nbr}
            return render(request,'zero_balance/zero_balance.html',context)
        else:
            message='脚本调用失败，请联系管理员！'
            context={'message':message,'number':nbr}
            return render(request,'zero_balance/zero_balance.html',context)
    return render(request,'zero_balance/zero_balance.html')

def day_bill(request):
    context = {}
    callType = '111'
    if request.method == 'POST':
        nbr=request.POST.get('number')
        starttime = request.POST.get('starttime').replace('-','')
        endtime = request.POST.get('endtime').replace('-','')
        datetime = str('-').join([starttime,endtime])
        #userType = request.POST.get('user_type')
        message = call_script('UserQuery',nbr,callType,datetime)
        print(nbr,datetime,userType)
        if message:
            context={'message':message,'number':nbr}
            return render(request,'day_bill/day_bill.html',context)
        else:
            message = '脚本调用失败，请联系管理员！'
            context={'message':message,'number':nbr}
            return render(request,'day_bill/day_bill.html',context)
    return render(request,'day_bill/day_bill.html')

def online_route(request):
    context = {}
    callType = '106'
    if request.method == 'POST':
        nbr = request.POST.get('number')
        #userType = request.POST.get('user_type')
        message = call_script('UserQuery',nbr,callType)
        if message:
            context = {'message':message,'number':nbr}
            return render(request,'online_route/online_route.html',context)
        else:
            message = '脚本调用失败，请联系管理员！'
            context = {'message':message,'number':nbr}
            return render(request,'online_route/online_route.html',context)
    return render(request,'online_route/online_route.html')

def account_route(request):
    context = {}
    callType = '107'
    if request.method == 'POST':
        nbr = request.POST.get('number')
        #userType = request.POST.get('user_type')
        message = call_script('UserQuery',nbr,callType)
        if message:
            context = {'message':message,'number':nbr}
            return render(request,'account_route/account_route.html',context)
        else:
            message = '脚本调用失败，请联系管理员！'
            context = {'message':message,'number':nbr}
            return render(request,'account_route/account_route.html',context)
    return render(request,'account_route/account_route.html')

def present(request):
    context={}
    callType = '109'
    if request.method == 'POST':
        actionCode=request.POST.get('actionCode')    
        #userType=request.POST.get('user_type')
        message = call_script('UserQuery',actionCode,callType)
        if message:
            context = {'message' : message,'actionCode':actionCode}
            return render(request,'present/present.html',context)
        else:
            message='脚本调用失败，请联系管理员！'
            context = {'message' : message,'actionCode':actionCode}
            return render(request,'present/present.html',context)
    return render(request,'present/present.html')

def bill(request):
    context = {}
    if request.method == 'POST':
        nbr=request.POST.get('number')
        starttime = request.POST.get('starttime').replace('-','')
        endtime = request.POST.get('endtime').replace('-','')
        datetime = str('-').join([starttime,endtime])
        #userType = request.POST.get('user_type')
        callType = request.POST.get('bill_type')
        message = call_script('UserQuery',nbr,callType,datetime)
        print(nbr,datetime,userType)
        if message:
            context={'message':message,'number':nbr}
            return render(request,'bill/bill.html',context)
        else:
            message = '脚本调用失败，请联系管理员！'
            context={'message':message,'number':nbr}
            return render(request,'bill/bill.html',context)
    return render(request,'bill/bill.html')


def user_route(request):
    context={}
    if request.method == 'POST':
        nbr = request.POST.get('number')
        callType = request.POST.get('route_type')
        #userType = 'ocs'
        print(nbr,callType)
        message = call_script('UserQuery',nbr,callType)
        if message:
            context = {'message':message,'number':nbr}
            return render(request,'user_route/user_route.html',context)
        else:
            message = '脚本调用失败，请联系管理员！'
            context = {'message':message,'number':nbr}
            return render(request,'user_route/user_route.html',context)
    return render(request,'user_route/user_route.html')
