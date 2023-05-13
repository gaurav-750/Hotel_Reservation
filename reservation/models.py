from django.db import models
from django.conf import settings


# Create your models here.
class Room(models.Model):
    TYPE_NORMAL = 'N'
    TYPE_DELUXE = 'D'
    ROOM_TYPE_CHOICES = [
        (TYPE_NORMAL, 'Normal'),
        (TYPE_DELUXE, 'Deluxe'),
    ]

    type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)
    number = models.IntegerField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True, blank=True)
    pricePerNight = models.IntegerField()
    size = models.IntegerField()
    maxOccupancy = models.IntegerField()
    discountPercentage = models.IntegerField(null=True, blank=True)
    isAvailable = models.BooleanField(default=True)
    description = models.TextField()
    balcony = models.BooleanField(default=False)
    parking = models.BooleanField(default=True)

    image = models.ImageField(upload_to='room_images/', blank=True, null=True)

    def __str__(self) -> str:
        return self.number + " " + self.type


class Reservation(models.Model):
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    User = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    CheckIn = models.DateField()
    Checkout = models.DateField()
    SpecialRequest = models.TextField()
    Cancelled = models.BooleanField(default=False)
    PaymentID = models.CharField(max_length=100, null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.Room.number + " " + self.User.username


class Customer(models.Model):
    User = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    dob = models.DateField()
    aadhar_id = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self) -> str:
        return self.User.username
