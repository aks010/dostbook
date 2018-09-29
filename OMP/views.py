from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):

 	return render(request,"index1.html")

def source(request):
 mname=request.GET.get("mname")
 a=[]
 b=os.listdir("OMP/static/songs/hollywood")
 for i in range(65,91):
 	a.append(chr(i))

 if mname=='bollywood':
 	return render(request,"index4.html",{"mname":mname,"lst":a})

 else:
 	return render(request,"index5.html",{"mname":mname,"lst":b})


def movies(request):
 mname=request.GET.get("mname")
 s="<html><body>"
 a=os.listdir("OMP/static/songs/bollywood")

 for i in a:
 	if i.startswith(mname):
 		s=s+"<a href='songs?mname="+i+"'>"+i+"</a><br>"
 s=s+"</body></html>"
 return HttpResponse(s)

def songs(request):
 mname=request.GET.get("mname")
 s="<html><body>"
 a=os.listdir("OMP/static/songs/bollywood/"+mname)
 return render(request,"index3.html",{"mname":request.GET.get("mname"),"lst":a})


def play(request):

 return render(request,"index2.html",{"mname":request.GET.get("mname"),"sname":request.GET.get("sname")})
