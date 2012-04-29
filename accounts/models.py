from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User

class UserProfile(models.Model):

    GREETINGS = (
        ('Mr.',   'Mr.'),
        ('Mrs.',  'Mrs.'),
        ('Ms.',   'Ms.'),
        ('Dr.',   'Dr.'),
        ('Prof.', 'Prof.'),
        ('Sir',   'Sir'),
    )
    
    user = models.ForeignKey(User, unique=True)

    greeting = models.CharField('Greeting',
                                max_length=5,
                                choices=GREETINGS,
                                blank=True)

    other_name = models.CharField('Other Names', max_length=100,blank=True)
    company = models.CharField('Company', max_length=100, blank=True)
    birthday = models.DateField('Birthday', blank=True, null=True)
    
    #TODO: we want only 0-9, '-', ' ', '.', 'x', 'ext', and '()' for phone.

    #from django.core.validators import RegexValidator
    #import re
    #phone_regex = re.compile(r'[^A-Za-z0-9 _.-()]+$') # Needs work
    #phone = models.CharField(max_length = 20, unique =False, blank=True,
    #                         validators=[RegexValidator(regex=phone_regex)] )

    phone = models.CharField('Phone number', max_length=50, blank=True)

    # Billing information
    bill_add_1 = models.CharField(max_length=200, blank=True)
    bill_add_2 = models.CharField(max_length=200, blank=True)
    bill_city = models.CharField(max_length=200, blank=True)
    bill_province = models.CharField(max_length=200, blank=True)
    bill_postal = models.CharField(max_length=6, blank=True)
    bill_country = models.CharField(max_length=200, blank=True)
    # TODO: Django-countries: http://code.google.com/p/django-countries/

    # Shipping information:
    # if True ignore shipping
    ship_as_bill = models.BooleanField(verbose_name="Ship to Billing?")
    ship_add_1 = models.CharField(max_length=200, blank=True)
    ship_add_2 = models.CharField(max_length=200, blank=True)
    ship_city = models.CharField(max_length=200, blank=True)
    ship_province = models.CharField(max_length=200, blank=True)
    ship_postal = models.CharField(max_length=6, blank=True)
    ship_country = models.CharField(max_length=200, blank=True)
    # TODO: Django-countries: http://code.google.com/p/django-countries/
        
    def __unicode__(self):
        return u'%s' % (self.user) # Note 'u' prefix

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
