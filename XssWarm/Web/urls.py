from Web import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$',views.login),
    url(r'^index$',views.index,name='index'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^commit$',views.comment,name='commit'),
    url(r'^getcommit$',views.getcommit,name='commit'),

]
