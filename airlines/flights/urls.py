from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name = "home"),
    path("<int:flight_id>",views.flight_det, name="flight_details"),
    path("book/<int:flight_id>", views.book, name = "flight_book")

]