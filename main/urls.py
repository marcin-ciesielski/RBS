from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', MyRoomListView.as_view(), name='room-list'),
    path('room/detail/<int:pk>', RoomDetailView.as_view(), name='room-detail'),
    path('room/new/', RoomCreateView.as_view(), name='room-new'),
    path('room/delete/<int:pk>', RoomDeleteView.as_view(), name='room-delete'),
    path('room/<int:pk>/edit/', RoomUpdateView.as_view(), name='room-edit'),
    path('room/search', SearchRoomView.as_view(), name='room-search'),
    path('booking/new/', BookingCreateView.as_view(), name='booking-new'),
]