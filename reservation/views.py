import cloudinary.uploader

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, DestroyModelMixin

from .serializers import RoomSerializer, ReservationSerializer, \
    CustomerSerializer, MyBookingSerializer
from .models import Room, Reservation, Customer


# Create your views here
class RoomView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    parser_classes = [MultiPartParser, FormParser]
    # permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        else:
            return [AllowAny()]

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


class RoomDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAdminUser()]


class ReservationView(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAdminUser]


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, req):
        (customer, created) = Customer.objects.get_or_create(User_id=req.user.id)
        if req.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif req.method == 'PUT':
            serializer = CustomerSerializer(customer, data=req.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class GetMyBookings(ListModelMixin,
                    DestroyModelMixin,
                    GenericViewSet):
    def get_queryset(self):
        return Reservation.objects.filter(User_id=self.request.user.id)
    serializer_class = MyBookingSerializer
    permission_classes = [IsAuthenticated]
