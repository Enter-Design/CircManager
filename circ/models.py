from django.db import models

from accounts.models import Customer

# Create your models here.

class Publication(models.Model):
    name = models.CharField(max_length=255, unique=True)
    issue_no = models.IntegerField(help_text='Current issue number')
    slug = models.SlugField(max_length=255, unique=True,
      help_text='Unique value for publication page URL, created from name.')
    price = models.DecimalField(max_digits=9,decimal_places=2)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('circ_publication', (), {'publication_slug':self.slug})

class Offer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,
      help_text='Unique value for offer page URL, created from name.')
    publication = models.ForeignKey(Publication)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    term = models.IntegerField(help_text='Number of issues')

    def __unicode__(self):
        return self.name



    

    
