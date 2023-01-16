from django.urls import path

from .views import HomeView#, CarDetailView

app_name = 'pages'

urlpatterns = [
    path('', HomeView, name='home'),
    #path('car-detail/', CarDetailView, name='car_detail'),
]
