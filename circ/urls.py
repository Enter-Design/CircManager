from django.conf.urls.defaults import *

from circ.models import Publication

urlpatterns = patterns('circ.views',
        (r'^$', 'index', { 'template_name':'circ/index.html'}, 'circ_home'),
        (r'^publication/(?P<publication_slug>[-\w]+)/$',
            'show_publication', {'template_name':'circ/publication.html'}, 'circ_publication'),
)
