from django.shortcuts import render
from django.contrib import messages

import requests

from .forms import CarForms

url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
payload = "{\n\t\"registrationNumber\": \"Sm18ebp\"\n}"
headers = {
                'x-api-key': 'LkmZehCC9z96eAkRtthdQ5fD0IAWsLyH9fQrJHSb',
                'Content-Type': 'application/json'
            }


def HomeView(request):
    if request.method == 'POST':
        form = CarForms(request.POST)
        if form.is_valid():
            form.save()
            response = requests.request("POST", url, headers=headers, data=payload)
            res = response.json()
            return render(request, 'detail_car.html', {'response': res})

        # not valid
        messages.warning(request, 'Please enter your information correctly')
        return render(request, 'home/home.html')

    # request get
    return render(request, 'home/home.html')
