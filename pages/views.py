from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

import logging
import requests

from .forms import CarForms

url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
headers = {
    'x-api-key': 'LkmZehCC9z96eAkRtthdQ5fD0IAWsLyH9fQrJHSb',
    'Content-Type': 'application/json'
}


def HomeView(request):
    if request.method == 'POST':
        form = CarForms(request.POST)
        if form.is_valid():
            form.save()
            try:
                tag = request.POST['tag']
                payload = "{\n\t\"registrationNumber\": \"%s\"\n}" % (tag, )
                response = requests.request("POST", url, headers=headers, data=payload)
                res = response.json()
                # not car
                if response.status_code == 400:
                    messages.error(request, 'There is no car')
                    return render(request, 'pages/home.html')
                ino doros konnnnn vaghti plak doros bod codeesh chiyee
                return render(request, 'pages/detail_car.html', {'response': res})
            # not connect api
            except Exception as e:
                logging.error(e)
                messages.warning(request, 'Please enter your license plate correctly')
                return render(request, 'pages/home.html')

        # not valid
        messages.warning(request, 'Please enter your information correctly')
        return render(request, 'pages/home.html')

    # request get
    return render(request, 'pages/home.html')


def CarDetailView(request):
    return render(request, 'pages/detail_car.html')
