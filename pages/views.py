from django.shortcuts import render
from django.contrib import messages

import logging
import requests

from .forms import CarForms


# API = application programming interface
url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
# header API
headers = {
    'x-api-key': 'LkmZehCC9z96eAkRtthdQ5fD0IAWsLyH9fQrJHSb',
    'Content-Type': 'application/json'
}


# home page
def HomeView(request):
    # request post
    if request.method == 'POST':
        form = CarForms(request.POST)

        # check valid data
        if form.is_valid():
            form.save()

            # request post to api
            try:
                tag = request.POST['tag']
                payload = "{\n\t\"registrationNumber\": \"%s\"\n}" % (tag,)
                response = requests.request("POST", url, headers=headers, data=payload)
                res = response.json()

                # not car
                if response.status_code == 400:
                    messages.error(request, 'There is no car')
                    return render(request, 'pages/home.html')

                # car valid ♥
                if response.status_code == 200:
                    return render(request, 'pages/detail_car.html', {'response': res})

            # not connect internet
            except Exception as e:
                logging.error(e)
                messages.warning(request, 'Please enter your license plate correctly')
                return render(request, 'pages/home.html')

        # not valid | 8 < x
        messages.warning(request, 'Please enter your information correctly')
        return render(request, 'pages/home.html')

    # request get
    return render(request, 'pages/home.html')


# page 2 car detail
def CarDetailView(request):
    return render(request, 'pages/detail_car.html')
