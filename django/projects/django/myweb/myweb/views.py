from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    print request.user.name
    return render_to_response('index.html',locals())
