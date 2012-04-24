from django.conf.urls.defaults import *

from circ.models import Publication, Offer

urlpatterns = patterns('circ.views',
        (r'^$', 'index', { 'template_name':'circ/index.html'}, 'circ_home'),
        (r'^publications/(?P<publication_slug>[-\w]+)/$',
            'show_publication', {'template_name':'circ/publication.html'}, 'circ_publication'),
        (r'^offers/(?P<offer_slug>[-\w]+)/$',
            'show_offer', {'template_name':'circ/offer.html'}, 'circ_offer'),
)
