from django.shortcuts import render_to_response

from circ.models import Publication, Subscription

def upcoming(request):

    #We don't actually have active / inactive publications yet!
    #active_publications = Publication.objects.filter(status__iexact='Active')
    active_publications = Publication.objects.all()

    for pub in active_publications:

        subs = Subscription.objects.filter(publication = pub)
        subs = subs.filter(end_issue__lte=pub.issue_no + 3)
        pub.subs = subs # Save this publications as subs. Is there a better way?
   
    return render_to_response('reports/upcoming.html',
                             {'publications': active_publications})
