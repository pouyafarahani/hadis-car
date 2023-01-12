from django.db import models


class CarModel(models.Model):
    tag = models.CharField(max_length=7)
    postal_code = models.CharField(max_length=20)
