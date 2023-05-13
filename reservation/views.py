import cloudinary.uploader

from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .serializers import RoomSerializer, ReservationSerializer
from .models import Room, Reservation, Customer


# Create your views here
class RoomView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # get image from request
            image = serializer.validated_data.get('image')

            if image:
                # upload image to cloudinary
                upload_result = cloudinary.uploader.upload(
                    image, folder="room_images/")
                image_url = upload_result['secure_url']

                # set cludinary image url to serializer
                serializer.validated_data['image'] = image_url

            # Save Room object to DB
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
