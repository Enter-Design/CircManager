from django.db import models

from circ.models import Subscription, Promo

# Create your models here.

class Payment(models.Model):

    PAYMENT_METHODS = (
        ('Credit', 'Credit card'),
        ('Cheque', 'Cheque'),
        ('Cash', 'Cash'),
        ('Gift', 'Gift card'),
        ('Paypal', 'Paypal'),
        ('Interac', 'Interac'),
    )

    subscription = models.ForeignKey(Subscription)
    method = models.CharField('Payment method',
                              max_length=7,
                              choices=PAYMENT_METHODS)

    promo = models.ForeignKey('products.Promo',
                                  verbose_name='Promo',
                                  related_name='subs_promo',
                                  blank=True, null=True)

    amount = models.DecimalField('Total',
                                 max_digits=9,
                                 decimal_places=2) # Max 9,999,999.99

    def __unicode__(self):
        return u'%s - %s for $%.2f' % (self.subscription,
                                       self.method,
                                       self.amount)
