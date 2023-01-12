from django.shortcuts import render
from django.contrib import messages

from .forms import CarForms


def HomeView(request):
    if request.method == 'POST':
        form = CarForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'detail_car.html')

        # not valid
        messages.warning(request, 'Please enter your information correctly')
        return render(request, 'home/home.html')

    # request get
    return render(request, 'home/home.html')
