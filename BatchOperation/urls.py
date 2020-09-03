from django.conf.urls import url
from BatchOperation import views


urlpatterns=[
    url(r'^upload_fille/',views.batch_operation,name='upload_fille'),
    url(r'sql_operation/',views.sql_operation,name='sql_operation'),
]
