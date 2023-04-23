from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey

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
#
class PType(models.Model):
    class Meta:
        verbose_name = 'PType'
        verbose_name_plural = 'PTypes'

    name = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return f'{self.name}'
#Cette class définit tous les groupes musculaires
class MuscleGroup(models.Model):
    class Meta:
        verbose_name = 'Muscle'
        verbose_name_plural = 'Muscles'
        ordering = ["name"]

    name = models.fields.CharField(blank=True, null=True, max_length=50)

    def exercises(self):
        return " / ".join(map(str, [e.name for e in ExoBody.objects.filter(muscle_group=self)[0:3]]))

    def __str__(self):
        return f'{self.name}'
#
class ExoHiit(models.Model):
    class Meta:
        verbose_name = 'Hiit-Exo'
        verbose_name_plural = 'Hiit-Exos'

    name = models.fields.CharField(blank=True, null=True, max_length=250)
    muscle_group = models.ForeignKey(MuscleGroup, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'[ {self.muscle_group.name} ] - {self.name}'
class ProgramHiit(models.Model):
    class Meta:
        verbose_name = 'Hiit-Program'
        verbose_name_plural = 'Hiit-Programs'

    LEVELS = [
        ("D", "[Débutant] - 20sec ON / 20sec OFF"),
        ("I", "[Intermédiaire] - 25sec ON / 15sec OFF"),
        ("A", "[Avancé] - 30sec ON / 10sec OFF"),
    ]
    PAUSES = [
        ("E", "30sec"),
        ("A", "1min"),
        ("I", "1min30"),
        ("D", "2mins"),
    ]
    title = models.fields.CharField(blank=True, null=True, max_length=100)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    program_type = models.fields.CharField(max_length=25, default='Hiit')
    level = models.CharField(max_length=2, choices=LEVELS, default="I")
    pause = models.CharField(max_length=2, choices=PAUSES, default="A")

    def __str__(self):
        return f'[ {self.title} ] - {self.customer}'
class FormHiit(models.Model):
    class Meta:
        verbose_name = 'Hiit-Form'
        verbose_name_plural = 'Hiit-Forms'

    program_hiit = models.ForeignKey(ProgramHiit, related_name="program_hiit", blank=True, null=True,on_delete=models.SET_NULL)
    set = models.IntegerField(null=True, default=2, verbose_name='Sets')
    exo_hiit = models.ForeignKey(ExoHiit, blank=True, null=True, on_delete=models.SET_NULL)

    # foreignkey class Program
    def title(self):
        return self.program_body.title

    def customer(self):
        return self.program_body.customer

    def program_type(self):
        return self.program_body.program_type

    def __str__(self):
        return f''
#Cette class définit tous les exercices associés à un groupe musculaire
class ExoBody(models.Model):
    class Meta:
        verbose_name = 'Body-Exo'
        verbose_name_plural = 'Body-Exos'

    name = models.fields.CharField(blank=True, null=True, max_length=250)
    muscle_group = models.ForeignKey(MuscleGroup, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'[ {self.muscle_group.name} ] - {self.name}'
class ProgramBody(models.Model):
    class Meta:
        verbose_name = 'Body-Program'
        verbose_name_plural = 'Body-Programs'

    title = models.fields.CharField(blank=True, null=True, max_length=100)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    program_type = models.fields.CharField(max_length=25, default='Bodybuilding')

    def __str__(self):
        return f'[ {self.title} ] - {self.customer}'
class FormBody(models.Model):
    class Meta:
        verbose_name = 'Body-Form'
        verbose_name_plural = 'Body-Forms'

    PAUSES = [
        ("AA", "30s"),
        ("A", "1min"),
        ("I", "1min30"),
        ("D","2mins"),
    ]

    TYPES = [
        ("NONE", "---------"),
        ("WARMUP", "Warm-up"),
        ("WOD", "Wod"),
    ]

    program_body = models.ForeignKey(ProgramBody, related_name="program_body", blank=True, null=True,on_delete=models.SET_NULL)
    type = models.CharField(max_length=10, choices=TYPES, default='NONE')
    set = models.IntegerField(null=True, default=2, verbose_name='Sets')
    rep = models.IntegerField(null=True, default=10, verbose_name='Reps')
    pause = models.CharField(max_length=2, choices=PAUSES, default="A")
    exo_body = models.ForeignKey(ExoBody, blank=True, null=True, on_delete=models.SET_NULL)

    # foreignkey class Program
    def title(self):
        return self.program_body.title

    def customer(self):
        return self.program_body.customer

    def program_type(self):
        return self.program_body.program_type

    def __str__(self):
        return f''

class ProgramMixte(models.Model):
    class Meta:
        verbose_name = 'Mixte-Program'
        verbose_name_plural = 'Mixte-Programs'

    title = models.fields.CharField(blank=True, null=True, max_length=100)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    program_type = models.fields.CharField(max_length=25, default='Mixte')

    def __str__(self):
        return f'[ {self.title} ] - {self.customer}'

    #exo_hiit = models.ForeignKey(ExoHiit, blank=True, null=True, on_delete=models.SET_NULL)
    #program_hiit = models.ForeignKey(ProgramHiit, blank=True, null=True, on_delete=models.SET_NULL)
