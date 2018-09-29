from django.db import models
from django.db import IntegrityError

# Create your models here.
class student(models.Model):
 name=models.CharField(max_length=50,default='SOME STRING')
 email=models.CharField(max_length=50)
 password=models.CharField(max_length=50)
 gender=models.CharField(max_length=50)
 state=models.CharField(max_length=50,default='SOME STRING')
 city=models.CharField(max_length=50)

class friends(models.Model):
 id = models.AutoField(primary_key=True)
 sender=models.CharField(max_length=50)
 receiver=models.CharField(max_length=50)
 status=models.IntegerField()

class post(models.Model):
 id=models.AutoField(primary_key=True)
 #sender=models.CharField(max_length=100)
 msg=models.CharField(max_length=500,blank=True,null=True)
 post_picture=models.ImageField(upload_to='post_picture/%y%m%d',null=True)
 sender=models.CharField(max_length=50)

class profpic(models.Model):
 id=models.AutoField(primary_key=True)
 emailid=models.CharField(max_length=50)
 profile_picture=models.ImageField(upload_to='profile_picture/%y%m%d', blank=True, null=True)
 status=models.IntegerField(default='0')
