"""Sensitive payroll intake remains disabled pending a secure data design."""

from django.http import HttpResponseGone


def get_social_security_number(request):
    """Return a permanent deprecation response; never accept or process SSNs here."""
    return HttpResponseGone(
        "Social Security number intake is disabled. Do not submit sensitive identifiers."
    )
