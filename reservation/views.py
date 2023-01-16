from django.shortcuts import render


def RezervView(request):
    FullService = request.POST['full']
    InterimService = request.POST['noll']
    return render(request, 'rezerv.html', {'FullService': FullService, 'InterimService': InterimService})
