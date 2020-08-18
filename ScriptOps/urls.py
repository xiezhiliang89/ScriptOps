"""ScriptOps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from catalog import views as catalog_views
from UserQuery import views as userquery_views
from StartUp import views as startup_views
from BatchOperation import views as batch_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^index/',include('catalog.urls')),
    url(r'^$',catalog_views.index,name='index'),
    url(r'^userquery/',include('UserQuery.urls')),
    url(r'^startup/',include('StartUp.urls')),
    url(r'batch/',include('BatchOperation.urls')),
]
