from django.conf.urls import url
from .views import index,report
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'report/$',report,name='report'),
    
]
