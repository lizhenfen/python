from django.conf.urls import url
from .views import index,manager,mulcmd,upfile
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'manager/$',manager,name='hostmgr'),
    url(r'mulcmd/$',mulcmd,name='mulcmd'),
    url(r'upfile/$',upfile,name='upfile'),
    
]
