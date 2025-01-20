import requests
import pandas as pd
from .models import FuelPrice
from django.db.models import F, FloatField, ExpressionWrapper
from django.db.models.functions import Cast

GOOGLE_MAPS_API_KEY = "AIzaSyAIg1C9jEgx0cUBJJ3YKq4zmywU2uqAqmc"

def get_lat_lng(city, state):
    """
    Fetch latitude and longitude from the Google Maps Geocoding API using city and state.
    """
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": f"{city}, {state}",
        "key": GOOGLE_MAPS_API_KEY,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    results = response.json().get("results", [])
    if results:
        location = results[0]["geometry"]["location"]
        return location["lat"], location["lng"]
    return None, None

def load_fuel_data():
    file_path = "/home/m4gici4nh4ck3r/Desktop/GitHub/Route-Fuel-Prices-Calculation-API/auto_entry/fuel-prices-for-be-assessment.csv"
    fuel_data = pd.read_csv(file_path)

    # Fetch existing IDs to minimize database queries
    existing_ids = set(FuelPrice.objects.values_list("opis_truckstop_id", flat=True))

    new_entries = []

    for _, row in fuel_data.iterrows():
        opis_truckstop_id = row["OPIS Truckstop ID"]

        # Skip if ID already exists
        if opis_truckstop_id in existing_ids:
            continue
            

        city = row["City"]
        state = row["State"]

        try:
            # Attempt to fetch latitude and longitude
            lat, lng = get_lat_lng(city, state)
            if lat is None or lng is None:
                print(f"Skipping entry for {city}, {state} due to missing coordinates.")
                continue  # Skip entries with null lat/lng

            print(f"Fuel data for {city}, {state} processed successfully.")
            # Add valid entry to the list
            new_entries.append(FuelPrice(
                opis_truckstop_id=opis_truckstop_id,
                truckstop_name=row["Truckstop Name"],
                address=row["Address"],
                city=city,
                state=state,
                rack_id=row["Rack ID"],
                retail_price=row["Retail Price"],
                latitude=lat,
                longitude=lng,
            ))

        except requests.exceptions.RequestException as e:
            print(f"Error fetching lat/lng for {city}, {state}: {e}")
            break  # Exit the loop on critical errors

        except Exception as generic_error:
            print(f"Unexpected error for {city}, {state}: {generic_error}")
            continue  # Skip problematic entries and continue processing

    # Save all new entries to the database
    if new_entries:
        try:
            FuelPrice.objects.bulk_create(new_entries, ignore_conflicts=True)
            print(f"{len(new_entries)} new fuel entries successfully saved.")
        except Exception as save_error:
            print(f"Error saving new entries: {save_error}")

    print("Fuel data processing completed!")

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

                print(location)

                # Query the database for the cheapest fuel station near the location
                fuel_stop = (
                    FuelPrice.objects.annotate(
                        # Ensure all fields and constants are treated as floats
                        distance=ExpressionWrapper(
                            (Cast(F("latitude"), FloatField()) - lat) ** 2 +
                            (Cast(F("longitude"), FloatField()) - lng) ** 2,
                            output_field=FloatField()
                        )
                    )
                    .order_by("distance", "retail_price")
                    .first()
                )

                print(fuel_stop)
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
