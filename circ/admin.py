from django.contrib import admin
from circ.models import Publication
from circ.forms import PublicationAdminForm

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
