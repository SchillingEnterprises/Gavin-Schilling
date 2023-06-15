from django.contrib import admin

from .models import Employee, TaxRate

admin.site.register(Employee)
admin.site.register(TaxRate)
