from django.urls import path


from .views import RezervView

app_name = 'reservations'


urlpatterns = [
    path('', RezervView, name='rezerv'),
]
