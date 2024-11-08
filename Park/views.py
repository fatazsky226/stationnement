from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Parking, Place
from .serializers import ParkingSerializer, PlaceSerializer

class ParkingStatusView(APIView):
    def get(self, request, parking_id):
        try:
            parking = Parking.objects.get(id=parking_id)
            serializer = ParkingSerializer(parking)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Parking.DoesNotExist:
            return Response({"error": "Parking not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, parking_id):
        try:
            parking = Parking.objects.get(id=parking_id)
            is_occupied = request.data.get("is_occupied", False)
            parking.statut = "occupé" if is_occupied else "libre"
            parking.save()
            return Response({"status": "success", "statut": parking.statut}, status=status.HTTP_200_OK)
        except Parking.DoesNotExist:
            return Response({"error": "Parking not found"}, status=status.HTTP_404_NOT_FOUND)
        

class PlaceListView(APIView):
    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

