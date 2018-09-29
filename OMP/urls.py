"""OMP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
#from django.contrib import admin
#rom django.conf import settings
#from django.conf.urls.static import static


#from OMP import views
from dostbook import views
urlpatterns = [
	# url(r'^admin/',admin.site.urls),
	# url(r'^index',views.index,name='index'),
	# url(r'^source',views.source,name='source'),
	# url(r'^movies',views.movies,name='movies'),
	# url(r'^songs',views.songs,name='songs'),
	# url(r'^play',views.play,name='play'),
    #url(r'^$',views.play,name='play'),
    # url(r'^$',views.newuser,name='home'),
    # url(r'^signup',views.signup,name='signup'),
    # url(r'^login',views.login,name='login'),
    # url(r'^login/welcomehome/',views.welcomehome,name='welpage'),
    # url(r'^login/welcomehome/friendrequest',views.friendrequest,name='friendrequest'),
    #url(r'^posts/',include("dostbook.urls")),
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
    url(r'^welcomehome/Editprofile/uploadpic$',views.uploadpic,name='uploadpic'),


    url(r'^welcomehome/Editprofile/modify/$',views.modify,name='modify'),

]
