from django.shortcuts import render
from .models import flights

def home(request):
    return render(request, 'flights/index.html',{
       'flights': flights.objects.all()
    })

def flight_det(request, flight_id):
    flight_details = flights.objects.get(pk = flight_id)
    passengers = flight_details.passengers.all()
    return render(request, 'flights/flight_detail.html',{
        'flight': flight_details,
        'passengers': passengers
    })


# Create your views here.
