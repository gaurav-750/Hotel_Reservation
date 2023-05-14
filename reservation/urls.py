from django.urls import path, include
from rest_framework_nested import routers

from .views import RoomView, ReservationView, CustomerViewSet, RoomDetailView


router = routers.DefaultRouter()
router.register('customers', CustomerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('rooms/', RoomView.as_view()),
    path('rooms/<int:pk>/', RoomDetailView.as_view()),
    path('reservations/', ReservationView.as_view()),
]
