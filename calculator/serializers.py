from rest_framework import serializers
from .models import FuelPrice

class FuelPriceSerializer(serializers.ModelSerializer):
    """Serializer for FuelPrice model."""

    class Meta:
        model = FuelPrice
        fields = [
            'id',
            'opis_truckstop_id',
            'truckstop_name',
            'address',
            'city',
            'state',
            'rack_id',
            'retail_price',
        ]

class OptimalFuelStopSerializer(serializers.Serializer):
    """Serializer for optimal fuel stop details."""
    name = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    retail_price = serializers.FloatField()
    cost_at_stop = serializers.FloatField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

class OptimalFuelStopsResponseSerializer(serializers.Serializer):
    """Serializer for the overall API response."""
    route = serializers.JSONField()
    stops = OptimalFuelStopSerializer(many=True)
    total_fuel_cost = serializers.FloatField()
