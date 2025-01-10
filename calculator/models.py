from django.db import models

class FuelPrice(models.Model):
    opis_truckstop_id = models.IntegerField(unique=True)  # Unique truck stop ID
    truckstop_name = models.CharField(max_length=255)  # Truck stop name
    address = models.TextField()  # Address
    city = models.CharField(max_length=100)  # City
    state = models.CharField(max_length=2)  # State
    rack_id = models.IntegerField()  # Rack ID
    retail_price = models.DecimalField(max_digits=10, decimal_places=6)  # Retail Price

    class Meta:
        indexes = [
            models.Index(fields=["city", "state"]),
            models.Index(fields=["retail_price"]),
        ]
    
    def __str__(self):
        return f"{self.truckstop_name} - {self.city}, {self.state}"
