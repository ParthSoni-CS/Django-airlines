from django.db import models

class airport(models.Model):
    city = models.CharField(max_length=40)
    code = models.CharField(max_length=40)

    def __str__(self):
        return f"Airport -> ({self.city},{self.code})"

class flights(models.Model):
    origin = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="departure")
    destination =  models.ForeignKey(airport, on_delete=models.CASCADE, related_name="arrival")
    duration =  models.IntegerField()

    def __str__(self):
        return f"FLights -> ({self.origin} to {self.destination})"

class passenger(models.Model):
    first_name =  models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    flight = models.ManyToManyField(flights,max_length=40, related_name="passengers")

    def __str__(self):
        return f"Passenger -> ({self.first_name} {self.last_name})"




# Create your models here.