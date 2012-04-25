from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

# import login_required shortcut
from django.contrib.auth.decorators import login_required

from models import UploadFileForm # import our upload form model

from subs.models import Customer
import os


def success(request):
    return render_to_response('uploader/success.html')

@login_required
def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # return a response from this page
            # name_list = handle_uploaded_file(request.FILES['file'])
            if handle_uploaded_file(request.FILES['file']):
                return HttpResponseRedirect('/upload/success/')
                # return render_to_response('uploader/results.html',
                # name_list,
                # context_instance=RequestContext(request))
            
    else:
        form = UploadFileForm()
    return render_to_response('uploader/index.html',
                              {'form': form},
                              context_instance=RequestContext(request))


def handle_uploaded_file(f):

    import os.path # Added to do away with abs path to templates, see below
    import csv # Let's read our CSV file the proper way using python
    # TODO import datetime # need to make sure our date inputs are valid

    # See os.path import, above. Builds a relative file name for our saved file
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    infile = os.path.join(SITE_ROOT, '../data/upload.txt')

    destination = open(infile, 'wb+')
    # This is how django (or python?) handles file uploads.
    for chunk in f.chunks():
        # We'll just write the chunks to a file, and re-open that file later
        destination.write(chunk)
        destination.close()

    with open(infile, "rb") as csvFile:

        csvSample = csvFile.read(1024) # Read sample for csv sniffer
        csvFile.seek(0)
        dialect = csv.Sniffer().sniff(csvSample)
        inReader = csv.reader(csvFile, dialect) # Read our .csv file

        # File must be opened in binary mode for has_header(file) to succeed.
        if csv.Sniffer().has_header(csvSample):
            inReader.next()
            #TODO I think we can use dictReader for this, would be better?
 
        import random # for username generation
        from django.contrib.auth.models import User
        import re # for username generation
        from datetime import datetime as dt

        for row in inReader:

            user_name = re.sub(r'\W+', '', row[1].lower())

            # We'd like usernames longer than 5 chars:
            if len(user_name) < 5: # First attempt, add last name
                user_name += re.sub(r'\W+', '', row[2].lower())
            if len(user_name) < 5: # Second attempt, add 3 digit rand int
                user_name += str(random.randrange(100,999))

            user_name = user_name[:30] # limit length per Django

            # if user exists, add rand digits. If too long, replace 2 chars.
            while User.objects.filter(username__iexact=user_name).count() > 0:
                user_name = user_name[:28] + str(random.randrange(99))

            pass_word = User.objects.make_random_password(10)

            user = User.objects.create_user(user_name,
                                            email=row[7],
                                            password=pass_word)

            user.first_name=row[1]
            user.last_name=row[2]
            user.is_staff=False
            user.is_active=False
            user.save()

            try: # YYYY-mm-dd format
                bd = dt.strptime(row[5], '%Y-%m-%d')
            except ValueError:
                pass
            try: # dd/mm/yy format
                bd = dt.strptime(row[5], '%m/%d/%y')
            except ValueError:
                bd = None

            c = Customer(
                user = user
                
                # Personal details
                , greeting=row[0] # doesn't seem to work? TODO
                , other_name=row[3]
                , company=row[4]
                , birthday=bd
                , phone=row[6]

                # Billing address:
                , bill_add_1=row[8], bill_add_2=row[9], bill_city=row[10]
                , bill_province=row[11]
                , bill_postal=row[12]
                , bill_country=row[13]
                
                # Shipping address:
                , ship_as_bill=row[14]
                , ship_add_1=row[15]
                , ship_add_2=row[16]
                , ship_city=row[17]
                , ship_province=row[18]
                , ship_postal=row[19]
                , ship_country=row[20]
                )
            c.save()

            # look for a product column
            # if none, check to see if we have a product defined in our DB
            # if not, define default product "MAGAZINE"

            #term_length = calculate_term(date)
            #p = Product(pk=1)
            #if not p:
            # p = Product(name='', term_length='', cost='')
            # p.save()
            #s = Subscription(payee_key=c, product_key=p, term_length)

    try:
        os.remove(infile) # Clean up temp file
    except:
        pass # Don't really care if delete fails

    # return {'name_list': ['mitch', 'ross', 'test']} # holy shit this worked.
    return True
