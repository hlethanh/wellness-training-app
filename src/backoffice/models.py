from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

#class User(AbstractUser):
    #address = models.fields.CharField(blank=True, null=True, max_length=250)

#Cette class définit les abonnés
class Customer(models.Model):
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    class Civility(models.TextChoices):
        M = 'M'
        Mme = 'Mme'

    civility = models.fields.CharField(choices=Civility.choices, blank=False, max_length=10)

    lastname = models.fields.CharField(blank=False, max_length=100)
    firstname = models.fields.CharField(blank=True, null=True, max_length=100)
    email = models.fields.EmailField(blank=False, max_length=254, unique=False)

    phone = models.fields.CharField(blank=False, max_length=15, unique=False)
    address = models.fields.CharField(blank=True, null=True, max_length=250)
    address_num = models.fields.IntegerField(blank=True, null=True)
    address_box = models.fields.IntegerField(blank=True, null=True)
    address_zip_code = models.fields.IntegerField(blank=True, null=True)
    address_city = models.fields.CharField(blank=True, null=True, max_length=250)
    address_country = models.fields.CharField(blank=True, null=True, max_length=250)
    birthday = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.lastname} {self.firstname}'

#Cette class définit tous les groupes musculaires
class MuscleGroup(models.Model):
    class Meta:
        verbose_name = 'Muscle'
        verbose_name_plural = 'Muscles'

    name = models.fields.CharField(blank=True, null=True, max_length=50)

    def all_exercises(self):
        return " / ".join(map(str, [s.name for s in MuscleGroupExo.objects.filter(muscle_group=self)[0:3]]))

    def __str__(self):
        return f'{self.name}'

#Cette class définit tous les exercices associés à un groupe musculaire
class MuscleGroupExo(models.Model):
    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'

    name = models.fields.CharField(blank=True, null=True, max_length=250)
    muscle_group = models.ForeignKey(MuscleGroup, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'[ {self.muscle_group.name} ] - {self.name}'
