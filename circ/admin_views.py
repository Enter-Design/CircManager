from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required

from circ.models import Publication, Offer, Subscription

def index(request, template_name='admin/circ/index.html'):
    page_title = 'deos da.'
    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))

def report(request):
    return render_to_response(
            "admin/circ/report.html",
            {'subscription_list': Subscription.objects.all()},
            RequestContext(request, {}),
    )

report = staff_member_required(report)
