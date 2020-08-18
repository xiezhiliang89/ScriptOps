from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def proxy_tool(request):
    if request.method=='POST':
        host=request.POST['host']
        print(type(host))
    return render(request,'proxy_tool.html')

