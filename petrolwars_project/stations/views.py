from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
stations = [
    {
        'name': 'ricky',
        'station': 'ricky petrol',
        'location': '123 A Street',
        'date_created': '19/03/2024'
    },

    {
        'name': 'ricky2',
        'station': 'rickys fuel',
        'location': '124 A Street',
        'date_created': '19/03/2024'
    }
]
def home(request):
    context = {
        "stations": stations
    }
    return render(request, 'stations/home.html', context)

def share(request):
    return render(request, 'stations/share.html', {'stations': 'share'})