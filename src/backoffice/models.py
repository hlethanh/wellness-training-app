from django.db import models
from datetime import date
from django.utils import timezone

#Cette class définit les abonnés
class Customer(models.Model):
    lastname = models.fields.CharField(blank=True, null=True, max_length=50)
    firstname = models.fields.CharField(blank=True, null=True, max_length=50)
    birthday = models.DateField(null=True, blank=True)
    weight = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.lastname} {self.firstname}'
