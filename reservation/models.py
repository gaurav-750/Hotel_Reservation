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

    # image = models.ImageField(upload_to='my-images', blank=True, null=True)
    # image = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)
