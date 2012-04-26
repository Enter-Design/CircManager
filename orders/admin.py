from django.contrib import admin
from django.contrib.auth.models import User

from orders.models import Payment

class PaymentAdmin(admin.ModelAdmin):
    
    pass

admin.site.register(Payment, PaymentAdmin)
