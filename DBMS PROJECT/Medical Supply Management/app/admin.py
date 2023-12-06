from django.contrib import admin
from .models import Contact,Medicines,ProductItems,MyOrders,DeliveredOrders
# Register your models here.
admin.site.register(Contact)
admin.site.register(Medicines)
admin.site.register(ProductItems)
admin.site.register(MyOrders)
admin.site.register(DeliveredOrders)