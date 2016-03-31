from django.conf.urls import url,include
from django.contrib import admin
from .views import index
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name='index'),
    url(r'^auth/',include('userauth.urls',namespace="auth")),
    url(r'^dashboard/',include('dashboard.urls',namespace="dashboard")),
    url(r'^hosts/',include('hosts.urls',namespace="hosts")),
    url(r'^assets/',include('assets.urls',namespace="assets")),
    url(r'^monitor/',include('monitor.urls',namespace="monitor")),
    
]
