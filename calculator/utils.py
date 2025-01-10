import requests
import pandas as pd
from .models import FuelPrice

def load_fuel_data():
    file_path = "/home/m4gici4nh4ck3r/Desktop/GitHub/Route-Fuel-Prices-Calculation-API/auto_entry/fuel-prices-for-be-assessment.csv"
    fuel_data = pd.read_csv(file_path)
    for _, row in fuel_data.iterrows():
        FuelPrice.objects.update_or_create(
            opis_truckstop_id=row["OPIS Truckstop ID"],
            defaults={
                "truckstop_name": row["Truckstop Name"],
                "address": row["Address"],
                "city": row["City"],
                "state": row["State"],
                "rack_id": row["Rack ID"],
                "retail_price": row["Retail Price"],
            },
        )
    print("Fuel data loaded successfully!")



GOOGLE_MAPS_API_KEY = "AIzaSyAIg1C9jEgx0cUBJJ3YKq4zmywU2uqAqmc"

def get_route(start_address, finish_address):
    """Fetch the route using a free map/routing API."""
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {"origin": start_address, "destination": finish_address, "key": GOOGLE_MAPS_API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    if not data["routes"]:
        raise ValueError("No route found.")
    
    return data
def calculate_fuel_stops(route, max_range=500, mpg=10):
    """
    Determine optimal fuel stops along the route.
    """
    stops = []
    total_cost = 0
    distance_covered = 0

    for leg in route["routes"][0]["legs"]:
        for step in leg["steps"]:
            distance_covered += step["distance"]["value"] / 1609.34  # meters to miles

            if distance_covered >= max_range:
                # Fetch latitude and longitude from the step's end location
                location = step["end_location"]
                lat, lng = location["lat"], location["lng"]

                # Use the Google Maps API to get city and state
                city, state = get_city_and_state({"lat": lat, "lng": lng})

                if city and state:
                    # Query the database for the cheapest fuel station in the city/state
                    fuel_stop = (
                        FuelPrice.objects.filter(city__iexact=city, state__iexact=state)
                        .order_by("retail_price")
                        .first()
                    )

                    if fuel_stop:
                        cost = (max_range / mpg) * float(fuel_stop.retail_price)
                        total_cost += cost
                        stops.append({
                            "truckstop_name": fuel_stop.truckstop_name,
                            "city": fuel_stop.city,
                            "state": fuel_stop.state,
                            "retail_price": float(fuel_stop.retail_price),
                            "cost": cost,
                        })

                        distance_covered = 0

    return stops, total_cost

def get_city_and_state(location):
    """
    Fetch city and state from the Google Maps Geocoding API using coordinates.
    """
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"{location['lat']},{location['lng']}",
        "key": GOOGLE_MAPS_API_KEY,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    results = response.json().get("results", [])

    if results:
        city = state = None
        for component in results[0]["address_components"]:
            if "locality" in component["types"]:  # City
                city = component["long_name"]
            if "administrative_area_level_1" in component["types"]:  # State
                state = component["short_name"]
        return city, state

    return None, None
