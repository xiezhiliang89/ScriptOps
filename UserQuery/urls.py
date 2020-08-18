from django.conf.urls import url
from UserQuery import views


urlpatterns=[
    url(r'^look/',views.look,name='look'),
    url(r'^pre_look/',views.pre_look,name='pre_look'),
    url(r'^zero_balance/',views.zero_balance,name='zero_balance'),
    #url(r'^day_bill/',views.day_bill,name='day_bill'),
    url(r'^bill/',views.bill,name='bill'),
    #url(r'online_route/',views.online_route,name='online_route'),
    #url(r'account_route/',views.account_route,name='account_route'),
    url(r'user_route/',views.user_route,name='user_route'),
    url(r'present/',views.present,name='present'),
    #url(r'user_bill/',views.user_bill,name='ubill'),
]
