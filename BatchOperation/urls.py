from django.conf.urls import url
from BatchOperation import views


urlpatterns=[
    url(r'^batch_operation/',views.batch_operation,name='batch_operation'),
    url(r'sql_operation/',views.sql_operation,name='sql_operation'),
]
