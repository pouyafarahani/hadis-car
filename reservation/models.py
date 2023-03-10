from django.db import models


class RezervModel(models.Model):
    # 3 ta service page book
    Full_service = models.BooleanField(default=False)
    Interim_service = models.BooleanField(default=False)
    Add_a_mot = models.BooleanField(default=False)

    # Which one do you want to fix?
    Wheelaligment = models.BooleanField(default=False)
    Diagnose = models.BooleanField(default=False)
    Tyres = models.BooleanField(default=False)
    Clutches = models.BooleanField(default=False)
    Suspension = models.BooleanField(default=False)
    Cambelt = models.BooleanField(default=False)
    Exhaust = models.BooleanField(default=False)
    Brakes = models.BooleanField(default=False)
    Batteries = models.BooleanField(default=False)

    # other ...
    other = models.TextField(null=True, blank=True)

    # User details
    Address = models.CharField(max_length=80)
    Firstname = models.CharField(max_length=80)
    Lastname = models.CharField(max_length=80)
    PhoneNumber = models.CharField(max_length=30)
    Email = models.EmailField(max_length=254, null=True, blank=True)
    Anything = models.TextField(null=True, blank=True)

    # car make
    make = models.CharField(max_length=10, null=True, blank=True)     # in model mashin hastesh
    register = models.CharField(max_length=20, null=True, blank=True)       # in ham pelak mashin hastesh
    # collection and delivery for free
    delivery = models.BooleanField(default=False)

    fixed = models.BooleanField(default=False)  # tamir shod

    def __str__(self):
        return self.Lastname
