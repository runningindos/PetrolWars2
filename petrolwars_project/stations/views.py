from django.shortcuts import render
from django.http import HttpResponse
from .models import Station

# Create your views here.
stations = [
    
]
def home(request):
    context = {
        "stations": Station.objects.all()
    }
    return render(request, 'stations/home.html', context)

def share(request):
    return render(request, 'stations/share.html', {'stations': 'share'})

