import cloudinary.uploader
from cloudinary.uploader import upload

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework import status

from .serializers import RoomSerializer

from .models import Room


# Create your views here


# class RoomView(ListCreateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
# parser_classes = (
#     MultiPartParser,
#     JSONParser,
# )

# # @staticmethod
# def post(self, request):
#     serializer = RoomSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=201)




class RoomView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            image = serializer.validated_data.get('image')

            if image:
                upload_result = cloudinary.uploader.upload(image, folder="room_images/")
                image_url = upload_result['secure_url']

                serializer.validated_data['image'] = image_url
            
            # Save Room object to DB
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)