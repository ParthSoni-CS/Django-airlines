from django.shortcuts import render, reverse
from .models import flights, passenger
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'flights/index.html',{
       'flights': flights.objects.all()
    })

def flight_det(request, flight_id):
    flight_details = flights.objects.get(pk = flight_id)
    passenger_detail = flight_details.passengers.all()
    return render(request, 'flights/flight_detail.html',{
        'flight': flight_details,
        'passengers': passenger_detail ,
        'npassengers': passenger.objects.exclude(flight = flight_details).all()

    })

def book(request, flight_id):
    if request.method == "POST":
        flight_info = flights.objects.get(pk = flight_id)
        passenger_info = passenger.objects.get(pk = int(request.POST["passenger-select"]))
        passenger_info.flight.add(flight_info)
        return HttpResponseRedirect(reverse("flight_details",args=(flight_id,)))





# Create your views here.
