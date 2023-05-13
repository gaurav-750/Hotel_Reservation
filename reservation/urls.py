from django.urls import path, include

from .views import RoomView, ReservationView

urlpatterns = [
    path('rooms/', RoomView.as_view()),
    path('reservations/', ReservationView.as_view())
]
