from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('home/',views.home),
    path('hotel/',views.hotel),

    
]
