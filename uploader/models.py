from django.db import models
from django.forms import ModelForm
from django import forms

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50) # don't forget to add it to the form
    file = forms.FileField()


class UploadFile(models.Model):
    title = models.CharField(max_length=50) # don't forget to add it to the form
    file = models.FileField(upload_to="data")
