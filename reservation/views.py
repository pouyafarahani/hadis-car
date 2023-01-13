from django.shortcuts import render


def RezervView(request):
    if request.method == 'POST':
        pass

    return render(request, 'rezerv.html')
