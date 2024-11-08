from rest_framework import serializers
from .models import Parking, Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'numero_place', 'taille', 'type_place', 'parking']



class ParkingSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)  # Inclure les places du parking

    class Meta:
        model = Parking
        fields = ['id', 'nom_parking', 'nombre_place', 'statut', 'places']
