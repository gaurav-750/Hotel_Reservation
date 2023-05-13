from rest_framework import serializers
from .models import Room, Reservation, Customer
from core.models import User


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'type', 'number', 'user', 'pricePerNight',
                  'size', 'maxOccupancy', 'isAvailable', 'description', 'balcony', 'parking',
                  'image', ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']


class ReservationSerializer(serializers.ModelSerializer):
    User = UserSerializer()

    class Meta:
        model = Reservation
        fields = ['id', 'Room', 'User', 'CheckIn', 'Checkout',
                  'SpecialRequest', 'Cancelled', 'PaymentID', 'TotalPrice']
