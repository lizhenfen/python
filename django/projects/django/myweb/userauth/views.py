from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse
from django.core import urlresolvers
from django.contrib.auth import authenticate,login,logout

def ulogin(request):
    if request.method == "GET":
        #return render_to_response('login.html')
        return render(request,'login.html')
    else:
        username = request.POST.get('email')
        password = request.POST.get('password')
        auth  = authenticate(username=username,password=password)
        if auth is not None:
            login(request,auth)
            return HttpResponseRedirect('/')
        else:
            return render(request,'login.html')
def ulogout(request):
    logout(request)
    return HttpResponseRedirect('/')
