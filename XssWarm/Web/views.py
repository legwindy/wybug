#!coding:utf-8

from django.shortcuts import render

# Create your views here.

from Web.models import *
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from Web.cookiecheck import authcheck


def login(request):
    return render(request,'login.html')

def index(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        docheck = user.objects.filter(user=username,password=password)
        if request.method =="POST" and docheck:
            request.session['user']=username
            rsp = render(request,'query.html',context={'username':username})
            rsp.set_signed_cookie('user',username,salt="hehehe")
            rsp.set_signed_cookie('logined','True',salt="hehehe")
            return rsp
        else:
            return render(request,'login.html')
    else:
        return HttpResponseRedirect("/")

@csrf_exempt
@authcheck
def getcommit(request):
     querylist = commit.objects.all()
     data = serializers.serialize("json",querylist)
     tempdata =str(data)
     final = tempdata.replace('\\\\','\\')
     return JsonResponse(final,safe=False)

def logout(request):
    rsp = render(request,'login.html')
    rsp.delete_cookie('user')
    rsp.delete_cookie('logined')
    return rsp

@csrf_exempt
@authcheck
def comment(request):
    text = request.POST["commit"]
    user = request.session['user']
    print user
    commit.objects.create(user=user,commit=text)
    return render(request,'query.html')

