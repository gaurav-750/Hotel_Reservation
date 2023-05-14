from django.urls import path, include
from rest_framework_nested import routers

from .views import RoomView, ReservationView, CustomerViewSet, RoomDetailView, GetMyBookings


router = routers.DefaultRouter()
router.register('customers', CustomerViewSet)
router.register('mybookings', GetMyBookings, basename='mybookings')

urlpatterns = [
    path('', include(router.urls)),
    path('rooms/', RoomView.as_view()),
    path('rooms/<int:pk>/', RoomDetailView.as_view()),
    path('reservations/', ReservationView.as_view()),
]
