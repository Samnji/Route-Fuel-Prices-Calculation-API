from django.urls import path
from .views import RouteFuelStopsAPIView

urlpatterns = [
    path("route-fuel-stops/", RouteFuelStopsAPIView.as_view(), name="route_fuel_stops"),
]
