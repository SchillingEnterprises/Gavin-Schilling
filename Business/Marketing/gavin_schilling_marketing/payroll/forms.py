from django import forms
from localflavor.us.forms import USPSSelect, USSocialSecurityNumberField, USStateSelect


class AddressForm(forms.Form):
    state = USStateSelect()
    postal_code = USPSSelect()


class SocialSecurityNumberForm(forms.Form):
    social_security_number = USSocialSecurityNumberField(max_length=9, min_length=9)
