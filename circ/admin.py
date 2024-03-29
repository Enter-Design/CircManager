from django.contrib import admin
from circ.models import Publication, Offer, Promo, Subscription
from circ.forms import PublicationAdminForm, OfferAdminForm

class PublicationAdmin(admin.ModelAdmin):
    form = PublicationAdminForm

    #sets values for how the admin site lists publications
    list_display = ('name', 'price', 'created_at',)
    list_display_links = ('name',)
    ordering = ['-created_at']
    search_fields = ['name', 'description']

    # sets up slug to be generated from product name
    prepopulated_fields = {'slug' : ('name',)}

# registers publication model with the admin site
admin.site.register(Publication, PublicationAdmin)

class OfferAdmin(admin.ModelAdmin):
    form = OfferAdminForm
    list_display = ('name', 'publication', 'term')
    list_display_links = ('name'),
    ordering = ['publication', 'name',]
    search_fields = ['publication', 'name',]
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Offer, OfferAdmin)

class PromoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Promo, PromoAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'publication', 'end_issue')
    list_display_links = ['subscriber',]
    search_fields = ['subscriber',]
    prepopulated_fields = {'slug' : ('subscriber', 'publication'),}

admin.site.register(Subscription)
