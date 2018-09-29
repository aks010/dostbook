from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
    url(r'^Create/$',views.post_create,name='post_create'),
    url(r'^Detail/$',views.post_detail,name='post_detail'),
    url(r'^Update/$',views.post_update,name='post_update'),
    url(r'^Delete/$',views.post_delete,name='post_delete'),
]
