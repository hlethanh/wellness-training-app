from django import forms
from django.forms import TextInput, Select
from backoffice.models import Customer, MuscleGroup

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('birthday','weight')  # ajoutez cette ligne
        widgets = {'civility': Select(attrs={'class': 'form-select'}),
                   'lastname': TextInput(attrs={'class': 'form-control'}),
                   'firstname': TextInput(attrs={'class': 'form-control'}),
                   'phone': TextInput(attrs={'class': 'form-control'}),
                   'email': TextInput(attrs={'class': 'form-control'}),

                   'address': TextInput(attrs={'class': 'form-control'}),
                   'address_num': TextInput(attrs={'class': 'form-control'}),
                   'address_box': TextInput(attrs={'class': 'form-control'}),

                   'address_zip_code': TextInput(attrs={'class': 'form-control'}),
                   'address_city': TextInput(attrs={'class': 'form-control'}),
                   'address_country': TextInput(attrs={'class': 'form-control'}),
                   'active': Select(choices=TRUE_FALSE_CHOICES, attrs={'class': 'form-select'}),
                   }
class MuscleForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = '__all__'
        widgets = {'name': TextInput(attrs={'class': 'form-control','style':'width:50%'})}