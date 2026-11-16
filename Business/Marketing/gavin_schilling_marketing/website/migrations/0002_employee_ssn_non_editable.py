# Generated to make the retained legacy SSN field non-editable.
from django.db import migrations
import localflavor.us.models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="social_security_number",
            field=localflavor.us.models.USSocialSecurityNumberField(
                blank=True,
                editable=False,
                max_length=11,
                null=True,
            ),
        ),
    ]
