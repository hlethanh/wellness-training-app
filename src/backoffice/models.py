from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

#Cette class définit les abonnés
class Customer(AbstractUser):
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    class Civility(models.TextChoices):
        M = 'M'
        Mme = 'Mme'

    #username = None
    username = models.fields.CharField(blank=True, max_length=100)
    civility = models.fields.CharField(choices=Civility.choices, blank=False, max_length=10)
    last_name = models.fields.CharField(blank=False, max_length=100)
    first_name = models.fields.CharField(blank=True, null=True, max_length=100)
    #email = models.fields.EmailField(unique=True)
    email = models.fields.EmailField(blank=False, max_length=254, unique=True)
    phone = models.fields.CharField(blank=False, max_length=15, unique=False)

    password = models.CharField(max_length=128, blank=True, null=True)

    address = models.fields.CharField(blank=True, null=True, max_length=250)
    address_num = models.fields.IntegerField(blank=True, null=True)
    address_box = models.fields.IntegerField(blank=True, null=True)
    address_zip_code = models.fields.IntegerField(blank=True, null=True)
    address_city = models.fields.CharField(blank=True, null=True, max_length=250)
    address_country = models.fields.CharField(blank=True, null=True, max_length=250)

    birthday = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

#Cette class définit tous les groupes musculaires
class MuscleGroup(models.Model):
    class Meta:
        verbose_name = 'Muscle'
        verbose_name_plural = 'Muscles'
        ordering = ["name"]

    name = models.fields.CharField(blank=True, null=True, max_length=50)

    def exercises(self):
        return " / ".join(map(str, [e.name for e in Exercise.objects.filter(muscle_group=self)[0:3]]))

    def __str__(self):
        return f'{self.name}'

#Cette class définit tous les exercices associés à un groupe musculaire
class Exercise(models.Model):
    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'

    name = models.fields.CharField(blank=True, null=True, max_length=250)
    muscle_group = models.ForeignKey(MuscleGroup, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'[ {self.muscle_group.name} ] - {self.name}'

class Hiit(models.Model):
    class Meta:
        verbose_name = 'Hiit'
        verbose_name_plural = 'Hiit'
        ordering = ["name"]

    name = models.fields.CharField(blank=True, null=True, max_length=250)
    muscle_group = models.ForeignKey(MuscleGroup, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'[ {self.muscle_group.name} ] - {self.name}'