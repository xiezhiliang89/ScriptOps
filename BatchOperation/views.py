from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.


def batch_operation(request):
    if request.method=='POST':
        businessType=request.POST['business-type']
        batchFile=request.FILES.get('batch_file')
        print(type(batchFile))
        print(businessType)
        filepath=os.path.join(r"/home/opsadmin/ScriptOps/BatchOperation/batch_fille",batchFile.name)
        f=open(filepath,mode='wb')
        for i in batchFile.chunks():
            f.write(i)
        f.close()
        return HttpResponse("ok")
    return render(request,'batch_operation.html')

def sql_operation(request):
    return 'hello world'
