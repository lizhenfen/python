from django.conf.urls import url
from .views import ulogout,ulogin
urlpatterns = [
    url(r'logout/$',ulogout,name='logout'),
    url(r'login/$',ulogin,name='login'),
    
]
