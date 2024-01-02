from django.db import models
from Register_Login.models import *
# Create your models here.

#---------------- models for zoho modules--------------------

class AddItem(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    type=models.TextField(max_length=255)
    Name=models.TextField(max_length=255)
    # unit=models.ForeignKey(Unit,on_delete=models.CASCADE)
    hsn=models.IntegerField(null=True,blank=True)
    # sales=models.ForeignKey(Sales,on_delete=models.CASCADE)
    minimum_stock=models.IntegerField(blank=True,null=True)  #---------------------> new field
    # purchase=models.ForeignKey(Purchase,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    s_desc=models.TextField(max_length=255)
    p_desc=models.TextField(max_length=255)
    creat=models.CharField(max_length=255)
    s_price=models.CharField(max_length=255)
    p_price=models.TextField(max_length=255)
    satus=models.TextField(default='active')
    interstate=models.CharField(max_length=255,default='')
    intrastate=models.CharField(max_length=255,default='')
    tax=models.TextField(max_length=255,null=True)
    invacc=models.TextField(max_length=255,null=True)
    stock=models.IntegerField(blank=True,null=True,default=0)
    rate=models.IntegerField(blank=True,null=True,)
    status_stock=models.TextField(default='active')