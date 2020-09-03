from django.shortcuts import render
from django.http import HttpResponse
import os
from .CallScript import call_script
# Create your views here.


def batch_operation(request):
    if request.method=='POST':
        businessType=request.POST['business-type']
        batchFile=request.FILES.getlist('batch_file')
        # print(type(batchFile))
        # print(businessType)
        # filepath=os.path.join(r"/ocs/opsadmin/ScriptOps/BatchOperation/batch_fille",batchFile.name)
        filepath="/ocs/opsadmin/ScriptOps/BatchOperation/batch_fille"
        result=[]
        for f in batchFile:
            dest=open(os.path.join(filepath,f.name),mode='wb')
            for c in f.chunks():
                dest.write(c)
            dest.close()
            
            result.append((f.name,os.path.exists(os.path.join(filepath,f.name))))
        
        context={'result':result}
        # return HttpResponse("<h2>文件上传成功</h2>")
        return render(request,'upload_fille.html',context)
    return render(request,'upload_fille.html')

def sql_operation(request):
    if request.method=="POST":
        sql='\"'+request.POST.get('sql')+'\"'
        buss_type=request.POST.get('business-type')
        message=call_script('BatchOperation',buss_type,sql)
        sql=sql.strip('\"')
        if message:
            context={'message':message,'sql':sql}
            return render(request,'sql_operation.html',context)
        else:
            message = '脚本调用失败，请联系管理员！'
            context = {'message':message,'sql':sql}
            return render(request,'sql_operation.html',context)
    return render(request,'sql_operation.html')
