from __future__ import unicode_literals

from django.db import models

# Create your models here.
class estimate(models.Model):
    service = models.CharField(max_length=30)
    product_id = models.CharField(max_length=250)
    display_name = models.CharField(max_length=30)
    max_cost = models.CharField(max_length=10)
    min_cost = models.CharField(max_length=10)
    range_estimate = models.CharField(max_length=20)
    currency = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    distance = models.CharField(max_length=10)


    def __str__(self):
        return self.display_name