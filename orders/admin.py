from django.contrib import admin
from orders.models import orders
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date','enroll_no', 'room', 'total_clothes')



admin.site.register(orders, OrderAdmin)

