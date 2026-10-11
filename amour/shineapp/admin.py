from django.contrib import admin
from .models import customer
class customerAdmin(admin.ModelAdmin):
        list_display=["customer_id","Name","productname","phoneno","Email","Address","Pincode"]
admin.site.register(customer,customerAdmin)        
