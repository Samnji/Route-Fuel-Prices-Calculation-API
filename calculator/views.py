from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_route, calculate_fuel_stops

class RouteFuelStopsAPIView(APIView):
    def post(self, request):
        start_address = request.data.get("start_address")
        finish_address = request.data.get("finish_address")

        if not start_address or not finish_address:
            return Response({"error": "Start and finish addresses are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            route = get_route(start_address, finish_address)
            fuel_stops, total_cost = calculate_fuel_stops(route)
            return Response({"fuel_stops": fuel_stops, "total_cost": total_cost}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
