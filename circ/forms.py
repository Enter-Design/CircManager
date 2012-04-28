from django import forms
from circ.models import Publication, Offer, Subscription
from django.contrib.auth.models import User

class PublicationAdminForm(forms.ModelForm):
    class Meta: 
        model = Publication

    # validation method to ensure price is greater than zero
    def clean_price(self):
        if self.cleaned_data['price'] < 0:
            raise forms.ValidationError('Price must be greater than or equal to zero.')
        return self.cleaned_data['price']

class OfferAdminForm(forms.ModelForm):
    class Meta:
        model = Offer

class SubscribeForm(forms.Form):
    """The subscribe form is used rather than the admin form
    because it allows for selection of an offer item rather than
    having to manually specifiy product, start & end issues."""

    subscriber = forms.ModelChoiceField(
                    required=True,
                    queryset=User.objects.all(),
                    widget=forms.Select)

    offer = forms.ModelChoiceField(
                    help_text='Select purchased product',
                    required=True,
                    queryset=Offer.objects.all(),
                    widget=forms.Select)

