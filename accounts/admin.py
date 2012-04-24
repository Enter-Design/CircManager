from django.contrib import admin
from django.contrib.auth.models import User

from accounts.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
