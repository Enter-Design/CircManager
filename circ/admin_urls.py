from django.conf.urls.defaults import *

urlpatterns = patterns('circ.admin_views',
        (r'^$', 'index', { 'template_name':'admin/circ/index.html'}, 'circ_home'),
        (r'^report/$', 'report'),
    )
