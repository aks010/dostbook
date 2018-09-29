from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns=[
    url(r'^$',views.newuser,name='home'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',views.login,name='login'),
    #url(r'^login/friendrequest/$',views.friendrequest,name='friendrequest'),
    #url(r'^login/accept',views.accept,name='accept'),
    #url(r'^login/removefriend',views.removefriend,name='removefriend'),
    #rl(r'^login/Editprofile/$',views.Editprofile,name='Editprofile'),
    #url(r'^login/Editprofile/modify/$',views.modify,name='modify'),

    url(r'^welcomehome/$',views.welcomehome,name='welcomehome'),
    url(r'^welcomehome/uploadpic',views.uploadpic,name='uploadpic'),
    url(r'^welcomehome/ajax1/$',views.ajax1,name='ajax1'),
    url(r'^welcomehome/savepost$',views.savepost,name='savepost'),
    url(r'^welcomehome/friendrequest/$',views.friendrequest,name='friendrequest'),
    url(r'^welcomehome/accept/$',views.accept,name='accept'),
    url(r'^welcomehome/reject/$',views.reject,name='reject'),
    url(r'^welcomehome/removefriend/$',views.removefriend,name='removefriend'),
    url(r'^welcomehome/Editprofile/$',views.Editprofile,name='Editprofile'),
    url(r'^welcomehome/Editprofile/modify/$',views.modify,name='modify'),
]
