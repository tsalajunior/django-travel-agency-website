from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, 'index.html')

def services(request, *args, **kwargs):
    return render(request, 'services.html')

def destinations(request, *args, **kwargs):
    return render(request, 'destinations.html')

def our_process(request, *args, **kwargs):
    return render(request, 'process.html')

def contact(request, *args, **kwargs):
    return render(request, 'contact.html')