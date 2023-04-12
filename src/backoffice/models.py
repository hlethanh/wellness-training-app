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

def customer_detail(request, id):
    customer = Customer.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Program avec cet id

    return render(request,
                  'backoffice/customer_detail.html',
                  {'customer': customer})

#Cette class définit tous les groupes musculaires
class MuscleGroup(models.Model):
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
