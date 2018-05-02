#!coding:utf-8

from Web import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$',views.login),
    url(r'^index$',views.index,name='index'),
    url(r'^doquery$',views.doquery,name='doquery'),
    url(r'^synchistory$',views.synchistory,name='synchistory'),
]
