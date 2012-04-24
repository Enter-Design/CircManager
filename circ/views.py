from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from circ.models import Publication

def index(request, template_name='circ/index.html'):
    page_title = 'Welcome to CircManager.'
    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))

def show_publication(request, publication_slug, template_name='circ/publication.html'):
    p = get_object_or_404(Publication, slug=publication_slug)
    page_title = p.name
    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))
