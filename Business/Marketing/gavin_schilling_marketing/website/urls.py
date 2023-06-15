from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('services/', views.services, name='services'),
    path('information_technology/network_engineering/', views.network_engineering, name='network_engineering'),
    path('information_technology/web_development/', views.web_development, name='web_development'),
    path('strategic_marketing/buzz_marketing/', views.buzz_marketing_service, name='buzz_marketing'),
]
