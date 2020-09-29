from django.shortcuts import render
from django.http import HttpResponse 
from django.http import FileResponse
import os
from .CallScript import call_script
# Create your views here.


def upload(request):
    if request.method=='POST':
        #businessType=request.POST['business-type']
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
        return render(request,'upload_file.html',context)
    return render(request,'upload_file.html')

def download(request):
    if request.method=='POST':
        filepath=request.POST.get('filepath')
        response=FileResponse(open(filepath,rb))
        response['Content-Type']='application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename={0}'.format(filepath.split('/')[-1])
        return response
    return render(request,'download_file.html')
    

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

def sql_file_operation(request):
    if request.method=="POST":
        buss_type = request.POST.get('business-type')
        if 'sqlfile_upload' in request.POST:
            #sql='\"'+request.POST.get('sql')+'\"'
            sqlFile = request.FILES.getlist('sql_file')
            filepath = "/ocs/opsadmin/ScriptOps/BatchOperation/sql_fille"
            result = []

            for f in sqlFile:
                dest = open(os.path.join(filepath, f.name), mode='wb')
                for c in f.chunks():
                    dest.write(c)
                dest.close()
                result.append((f.name, os.path.exists(os.path.join(filepath, f.name))))
            context = {'result': result}

            message = call_script('SqlFileOperation', buss_type, sqlFile)
            if message:
                context.update({'message': message})
                return render(request, 'sql_file_operation.html', context)
            return render(request, 'sql_file_operation.html', context)

        # elif 'sqlfile_exec' in request.POST:
        #     message=call_script('SqlFileOperation',buss_type,sqlFile)
        #     if message:
        #         context={'message':message}
        #         return render(request,'sql_file_operation.html',context)
        #     else:
        #         message = '脚本调用失败，请联系管理员！'
        #         context = {'message':message}
        #         return render(request,'sql_file_operation.html',context)
    return render(request,'sql_file_operation.html')

