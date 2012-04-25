from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()



urlpatterns = patterns('',
    # url(r'^myapp/', include('myapp.urls')),
    
    # Home Page -- Replace if you like
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # Circ app urls
    url(r'^circ/', include('circ.urls')),

    # Circ app admin urls
    url(r'^admin/circ/', include('circ.admin_urls')),

    # Report app
    url(r'^reports/upcoming/', 'reports.views.upcoming'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^upload/upload/', 'uploader.views.upload_file', name='upload'),
    url(r'^upload/success/', 'uploader.views.success', name='success'),

)
