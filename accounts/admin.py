from django.contrib import admin
from django.contrib.auth.models import User

from accounts.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
