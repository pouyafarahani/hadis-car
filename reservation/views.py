from django.shortcuts import render
from django.contrib import messages

from .forms import RezervForm


def RezervView(request):
    # request post
    if request.method == 'POST':
        form = RezervForm(request.POST)

        # data valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been successfully registered')  # رزرو شما با موفقیت ثبت شد
            return render(request, 'pages/home.html')

        # deta not valid
        else:
            print(form)
            messages.warning(request, 'Your information is not correct')  # اطلاعات شما صحیح نیست !
            return render(request, 'rezerv.html', {'forms': form})

    # request get | price service
    FullService = request.GET['FullService']
    InterimService = request.GET['InterimService']
    return render(request, 'rezerv.html', {'FullService': FullService, 'InterimService': InterimService})
