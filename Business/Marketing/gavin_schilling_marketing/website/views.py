from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def clients(request):
    return render(request, 'website/clients.html')


def services(request):
    return render(request, 'website/services.html')


def network_engineering(request):
    return render(request, 'website/services/information_technology/network_engineering.html')


def web_development(request):
    return render(request, 'website/services/information_technology/web_development.html')


def buzz_marketing_service(request):
    return render(request, 'website/services/strategic_marketing/buzz_marketing.html')
