from django.shortcuts import render


def CarDetailView(request):
    return render(request, 'detail_car.html')
