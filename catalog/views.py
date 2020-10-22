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
            ("CB用户信息(mysql)","/userquery/look"),
            ("CB用户赠送信息(oracle)","/userquery/pre_look"),
            #("零点余额","/userquery/zero_balance"),
            #("账单查询","/userquery/bill"),
            ("赠送活动查询(timesten)","/userquery/present"),
            ("在线proxy路由查询(proxy)","/userquery/user_route"),
        ),
         (
             ("AOP接口日志查询",''),
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
            #("账户信息修改",''),
            #("产品信息变更",''),
            ("SQL操作","/batch/sql_operation"),
        ),
        (
            ("SQL文件操作",'/batch/sql_file_operation'),
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
                "batch_sql_change":OPERATION_BODY[1],
                "batch_change": OPERATION_BODY[2],
            }
    )
    return render(request,'index.html',context)
