from uploader.models import UploadFileForm, UploadFile
from django.contrib import admin

class UploadFileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UploadFile, UploadFileAdmin)
