from django.shortcuts import render,render_to_response
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render_to_response('hosts/hostmgr.html',locals())
    #return render_to_response('hosts/index.html',locals())
def manager(request):
    return render_to_response('hosts/hostmgr.html',locals())
  
def mulcmd(request):
    return render_to_response('hosts/multicmd.html',locals())
def upfile(request):
    return render_to_response('hosts/hostmgr.html',locals())
