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


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'User', 'mobile', 'dob', 'aadhar_id', 'address']


class SimpleRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'type', 'number', 'pricePerNight',
                  'size', 'maxOccupancy', 'description', 'balcony',
                  'image',]


class MyBookingSerializer(serializers.ModelSerializer):
    Room = SimpleRoomSerializer()

    class Meta:
        model = Reservation
        fields = ['id', 'Room', 'CheckIn', 'Checkout',
                  'SpecialRequest', 'Cancelled', 'PaymentID', 'TotalPrice']
