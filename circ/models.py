from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Publication(models.Model):
    name = models.CharField(max_length=255, unique=True)
    issue_no = models.IntegerField(help_text='Current issue number',
                                   verbose_name='Current Issue Number')
    slug = models.SlugField(max_length=255, unique=True,
        help_text='Unique value for publication page URL, created from name.')
    price = models.DecimalField(max_digits=9,
                                decimal_places=2,
                                help_text='Suggested single issue price')
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
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

class Promo(models.Model):

    name = models.CharField('Promo name', max_length=200)
    dateCreated = models.DateField('Created', blank=True, null=True)
    # TODO: Limit discount to max 100
    discount = models.PositiveIntegerField(
            help_text="% discount (ex: '20')")
    description = models.TextField()

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.discount)    

class Subscription(models.Model):
    """Ties publication to a customer with a start issue and an end issue."""

    subscriber = models.ForeignKey(User)
    publication = models.ForeignKey('Publication')
    slug = models.SlugField(max_length=255, unique=True,
      help_text = 'Unique value for Subscription URL.')
    first_issue = models.IntegerField() # inclusive
    end_issue = models.IntegerField() # inclusive
    
    STATUSES = (
        ('Inactive', 'Inactive'),
        ('Active', 'Active'),
        ('Closed', 'Closed'),
        ('Hold', 'Hold'),
    )

    status = models.CharField('Status', max_length=8,
                              choices=STATUSES,
                              default='Active')

    def __unicode__(self):
        return u'%s - %s: %s:%s' % (self.subscriber,
                                    self.publication,
                                    self.first_issue,
                                    self.end_issue)
