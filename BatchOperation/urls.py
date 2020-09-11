from django.conf.urls import url
from BatchOperation import views


urlpatterns=[
    url(r'^upload_file/',views.upload,name='upload_file'),
    url(r'^download_file',views.download,name='download_file'),
    url(r'sql_operation/',views.sql_operation,name='sql_operation'),
    url(r'sql_file_operation/',views.sql_file_operation,name='sql_file_operation'),
]
