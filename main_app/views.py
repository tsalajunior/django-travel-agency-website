import json

from django.conf import settings
from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, 'index.html')

def services(request, *args, **kwargs):
    with (settings.BASE_DIR / 'data.json').open(encoding='utf-8') as data_file:
        data = json.load(data_file)

    services = list(data['services'].values())
    return render(request, 'services.html', {'services': services})

def destinations(request, *args, **kwargs):
    with (settings.BASE_DIR / 'data.json').open(encoding='utf-8') as data_file:
        data = json.load(data_file)

    destinations = list(data['destinations'].values())
    return render(request, 'destinations.html', {'destinations': destinations})

def our_process(request, *args, **kwargs):
    return render(request, 'process.html')

def contact(request, *args, **kwargs):
    return render(request, 'contact.html')