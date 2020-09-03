from django.shortcuts import render
from django.http import HttpResponse
#Create your views here.

APP_HEAD=[
        ("信息查询","#panel-91423"),
        ("应用管理","#panel-182157"),
        ("数据操作","#panel-190315"),
        #("终端","#panel-190409"),

]
QUERY_BODY=[
        (
            ("用户信息","/userquery/look"),
            ("用户活动","/userquery/pre_look"),
            ("零点余额","/userquery/zero_balance"),
            ("账单查询","/userquery/bill"),
            ("用户路由","/userquery/user_route"),
            ("赠送活动查询","/userquery/present"),
        ),
        (
            ("接口日志查询",''),
            ("Proxy日志查询",''),
        ),
]
STARTUP_BODY=[
        (
            ("proxy_tool","/startup/proxy_tool"),
        ),
        (
            ("应用启停",""),
        )
]

OPERATION_BODY=[
        (
            ("账户信息修改",''),
            ("产品信息变更",''),
            ("SQL操作","/batch/sql_operation")
        ),
        (
            ("文件上传",'/batch/upload_file'),
            ('文件下载','/batch/download_file'),
        )
]
def index(request):
    context=dict(
            {
                "tabs":APP_HEAD,
                "user_info":QUERY_BODY[0],
                "log_info":QUERY_BODY[1],
                "proxy_tool":STARTUP_BODY[0],
                "app_tool":STARTUP_BODY[1],
                "info_change":OPERATION_BODY[0],
                "batch_change":OPERATION_BODY[1],
            }
    )
    return render(request,'index.html',context)
