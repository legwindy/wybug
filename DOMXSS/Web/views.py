#!coding:utf-8

from django.shortcuts import render

# Create your views here.

from Web.models import *
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.core import serializers
import json

def login(requst):
    return render(requst,'login.html')

def index(requst):
    if requst.method =="POST":
        username = requst.POST["username"]
        password = requst.POST["password"]
        docheck = user.objects.filter(user=username,password=password)
        if requst.method =="POST" and docheck:
            querylist = query.objects.all()
            return render(requst,'query.html',context={'querylist':querylist})
        else:
            return render(requst,'login.html')
    else:
        return HttpResponseRedirect("/")

def doquery(request):
    querylist = query.objects.all()
    querys = request.GET["Search"]
    queryhistoy.objects.create(name=querys)
    return render(request,'query.html',context={'querylist':querylist})


def synchistory(request):
    querysets =queryhistoy.objects.all()
    #使用django原生的json序列化会转义\导致此例中的DOMXSS失效
    data = serializers.serialize("json",querysets)
    tempdata =str(data)
    final = tempdata.replace('\\\\','\\')
    final = final.replace('<','&lt')
    return JsonResponse(final,safe=False)
