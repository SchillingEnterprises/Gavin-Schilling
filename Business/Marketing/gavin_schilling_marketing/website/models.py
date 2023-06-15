from django.db import models
from django.utils.translation import gettext_lazy as _
from address.models import AddressField, Locality, Country
from localflavor.us.models import USPostalCodeField, USStateField, USSocialSecurityNumberField
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    name = models.CharField(max_length=200)
    headquarters_address = AddressField(blank=True)
    main_line = PhoneNumberField(blank=True)
    website_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "companies"


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)

    street_address = AddressField(name='Street Address', blank=True)
    city = Locality(name='City')
    state = USStateField(name='State', blank=True)
    country = Country(name='Country')
    zip_code = USPostalCodeField(name='Zip Code', blank=True, null=True)

    extension_line = PhoneNumberField(blank=True)
    cell_phone = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    personal_profile = models.URLField(blank=True)


class Employee (models.Model):
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)

    street_address = AddressField(name='Street Address', blank=True)
    state = USStateField(name='State')
    zip_code = USPostalCodeField(name='Zip Code', blank=True, null=True)

    gender = models.CharField(max_length=7)
    social_security_number = USSocialSecurityNumberField(blank=True, null=True)

    class EmploymentType(models.TextChoices):
        W2 = 'W-2', _('Employee')
        Form_1099 = '1099', _('Independent Contractor')
        C2C = 'C2C', _('Corp-to-Corp')

    employment_type = models.CharField(
        max_length=4,
        choices=EmploymentType.choices,
        default=EmploymentType.Form_1099,
    )

    def __str__(self):
        return f'{self.last_name}, {self.first_name} {self.middle_name}'
