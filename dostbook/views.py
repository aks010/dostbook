from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student,friends,post,profpic
from django.db.models import Q
import copy
# Create your views here.
def newuser(request):
 return render(request,"signup.html")

def signup(request):

    s=student()
    email=request.GET.get("email")
    password=request.GET.get("password")
    name=request.GET.get("name")

    a=student.objects.filter(email=email)
    if (email=="" or password=="" or name==""):
        return HttpResponse("please fill required field")
    elif (a.exists()==False):
         s.name=request.GET.get("name")
         s.email=request.GET.get("email")
         s.password=request.GET.get("password")
         s.gender=request.GET.get("gender")
         s.city=request.GET.get("city")
         s.save()
         return HttpResponse("SUCCESSFULLY SIGNED UP")
    else:
         return HttpResponse("RETRY-EMAIL ID ALREADY EXISTS ")
         # return redirect('home')

def login(request):

    uemail=request.GET.get("uemail")
    upassword=request.GET.get("upassword")
    request.session['semail']=uemail
    #semail=request.session['semail']
    students=student.objects.filter(email=uemail,password=upassword)
    if uemail=="" or upassword=="" :
        return HttpResponse("Please fill required field")
    elif students.exists()==True:
        #return HttpResponse(semail)
        return HttpResponse("VALID")
    else:
        return HttpResponse("INVALID")
        #return render("request","Error.html


def welcomehome(request):
    uemail=request.session.get('semail')
    s=student.objects.all()
    f=friends.objects.filter(receiver=uemail,status=0)
    friendlist=GetFriends(request.session.get('semail'))
    z=friends.objects.filter(Q(sender=uemail)|Q(receiver=uemail ),status=1)


    list=copy.deepcopy(friendlist)
    friendlist.append(uemail)
    post=viewpost(friendlist)
    a=dict()
    for aa in z:
        for bb in list:
            if bb==aa.sender or bb==aa.receiver :
                a[aa.id]=bb




    pp=profpic.objects.filter(emailid=request.session.get('semail'),status=1)
    return render(request,"Welcome.html",{"s":s,"f":f,"a":a,"post":post,"pp":pp})



def ajax1(request):
    entry=request.GET.get("name")
    p=student.objects.filter(email__startswith=entry).exclude(email=request.session.get('semail'))

    ll="<select size='10' onchange='disp1(this.value)'>"
    for a in p:
        ll=ll+"<option>"+a.email+"</option>"
    ll=ll+"</select>"
    return HttpResponse(ll)



def friendrequest(request):

    semail=request.session['semail']
    f=friends()
    f.sender=semail
    f.receiver=request.GET.get("search")
    f.status=0
    f.save()
    return redirect('welcomehome')


def Editprofile(request):
    return render(request,"Editprofile.html")

def modify(request):
    semail=request.session['semail']
    s=student.objects.get(email=semail)
    s.password=request.GET.get('pass')
    s.save()
    return HttpResponse("saved")
def accept(request):
    id=request.GET.get("request")
    #semail=request.session['semail']
    f=friends.objects.get(id=id)
    f.status=1
    f.save()
    return redirect('welcomehome')
    #return render(request,"accept.html")
def reject(request):
    id=request.GET.get("request")
    #semail=request.session['semail']
    f=friends.objects.get(id=id)
    f.status=2
    f.save()
    return redirect('welcomehome')


def removefriend(request):
    #semail=request.session['semail']
    id=request.GET.get("name")
    f=friends.objects.get(id=id)
    f.status=2
    f.save()
    return redirect('welcomehome')
def GetFriends(uid):
    fri=[]
    z=friends.objects.filter(Q(sender=uid)|Q(receiver=uid),status=1)
    for ff in z:
        if ff.sender==uid:
            fri.append(ff.receiver)
        else:
            fri.append(ff.sender)
    return fri

def savepost(request):
    if request.method == 'POST':
        msg1=request.POST.get("msg")
        sender1=request.session.get("semail")
        pic=request.FILES.get('myfile1')
        post_obj=post(post_picture=pic,sender=sender1,msg=msg1).save()
    return redirect('welcomehome')

def viewpost(list):
    p=post.objects.all()
    mypost=[]
    for a in p:
        if list.count(a.sender)>0:
            mypost.append(a)

    return mypost



def uploadpic(request):

    if request.method == 'POST':
            pp=profpic.objects.filter(emailid=request.session.get('semail'),status=1)
            for a in pp:
                a.status=0
                a.save()
            emails=request.session.get("semail")
            pic=request.FILES.get('myfile')
            status=1
            profile_obj=profpic(profile_picture=pic,emailid=emails,status=status).save()
    return redirect('welcomehome')
