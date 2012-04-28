from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from circ.models import Publication, Offer, Subscription
from circ.forms import SubscribeForm

import re   # slug generation

def index(request, template_name='circ/index.html'):
    page_title = 'Welcome to CircManager.'
    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))

def show_publication(request,
        publication_slug, template_name='circ/publication.html'):
    p = get_object_or_404(Publication, slug=publication_slug)
    page_title = p.name
    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))

def show_offer(request, offer_slug, template_name='circ/offer.html'):
    o = get_object_or_404(Offer, slug=offer_slug)
    page_title = o.name
    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))

def show_subscription(request,
        subscription_slug, template_name='circ/subscription.html'):
    s = get_object_or_404(Subscription, slug=subscription_slug)
    page_title = s.slug
    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))

def subscribe(request):

    if request.method == 'POST':
        
        form = SubscribeForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            prod = cd['offer'].publication

            the_slug = (cd['subscriber'].username + '-' + prod.name).lower()
            the_slug = re.sub(r'\W+', '-', the_slug)

            subscription = Subscription(
                subscriber = cd['subscriber'],
                publication = prod,
                first_issue = prod.issue_no,
                end_issue = prod.issue_no + cd['offer'].term,
                slug = the_slug,
                status = 'Active')

            subscription.save()

            return render_to_response('circ/subscribe.html',{
                                      'success': True,
                                      'subscription': subscription
                                      })

    else:
        form = SubscribeForm()
    return render_to_response('circ/subscribe.html',
                              {'form': form},
                              context_instance=RequestContext(request))
