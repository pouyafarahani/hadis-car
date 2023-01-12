from django.urls import path

from .views import CarDetailView

app_name = 'car_detail'


urlpatterns = [
    path('', CarDetailView, name='car_detail'),
]
