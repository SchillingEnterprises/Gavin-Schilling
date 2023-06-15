from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator
from website.models import Client, Company, Employee


class TimeSheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True)

    pay_rate = MoneyField(
        max_digits=6,
        decimal_places=2,
        default_currency='USD',
        validators=[
            MinMoneyValidator({'USD': 0.01})
        ],
    )

    work_duration = models.DecimalField(name='Duration of Work', max_digits=6, decimal_places=3)


class TaxRate (models.Model):
    """ Federal Taxes """
    social_security = models.DecimalField(name='Social Security', max_digits=3, decimal_places=1)
    medicare = models.DecimalField(name='Medicare', max_digits=3, decimal_places=2)
