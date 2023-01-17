from django.contrib import admin

from .models import RezervModel
# Register your models here.
# admin.site.register(RezervModel)


@admin.register(RezervModel)
class RezervAdmin(admin.ModelAdmin):
    list_display = ['Firstname', 'Lastname', 'PhoneNumber', 'make', 'delivery']
