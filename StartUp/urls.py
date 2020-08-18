from django.conf.urls import url
from StartUp import views


urlpatterns=[
    url(r'^proxy_tool/',views.proxy_tool,name='proxy_tool'),
]
