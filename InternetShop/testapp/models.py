from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25)
    count = models.IntegerField()
    cost = models.DecimalField(decimal_places=2, max_digits=10)
