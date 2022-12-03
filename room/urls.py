from django.urls import path
from . import views

__author__ = 'BENZNANA Mohamed : benznana.med@gmail.com'


urlpatterns = [
    path('', views.RoomsView.as_view(), name='rooms'),
    path('<slug:slug>/', views.RoomView.as_view(), name='room'),
]