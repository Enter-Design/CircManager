from django import forms
from circ.models import Publication, Offer, Subscription

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
