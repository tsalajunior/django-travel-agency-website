from django.urls import path

from main_app.views import *

urlpatterns = [
	path('', home, name='home'),
    path('services/', services, name='services'),
    path('destinations/', destinations, name='destinations'),
    path('process/', our_process, name='our_process'),
    path('contact/', contact, name='contact'),
]
