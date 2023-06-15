from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SocialSecurityNumberForm


def get_social_security_number(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SocialSecurityNumberForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SocialSecurityNumberForm()

    return render(request, 'forms/ssn.html', {'form': form})