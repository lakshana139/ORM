from django.db import models
from django.contrib import admin
class customer(models.Model):
    customer_id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=10)
    productname=models.CharField()
    phoneno=models.IntegerField()
    Email=models.EmailField()
    Address=models.TextField()
    Pincode=models.IntegerField()
    class customerAdmin(admin.ModelAdmin):
        list_display=["customer_id","Name","productname","phoneno","Email","Address","Pincode"]