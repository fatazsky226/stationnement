from django.urls import path
from .views import ParkingStatusView, PlaceListView



urlpatterns = [
    path('api/parking/<int:parking_id>/status/', ParkingStatusView.as_view(), name='parking_status'),
    path('api/places/', PlaceListView.as_view(), name='place_list'),
]
