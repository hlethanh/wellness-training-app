from django import forms
from django.forms import TextInput, Select
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from backoffice.models import Customer, MuscleGroup, ExoBody, ExoHiit

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)
class CustomerCreateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = (
            'civility', 'last_name', 'first_name', 'email', 'phone', 'is_active',
            'address', 'address_num', 'address_box', 'address_zip_code', 'address_city', 'address_country'
        )

        widgets = {
            'civility': Select(attrs={'class': 'form-select'}),

            'last_name': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'is_active': Select(choices=TRUE_FALSE_CHOICES, attrs={'class': 'form-select'}),

            'address': TextInput(attrs={'class': 'form-control'}),
            'address_num': TextInput(attrs={'class': 'form-control'}),
            'address_box': TextInput(attrs={'class': 'form-control'}),
            'address_zip_code': TextInput(attrs={'class': 'form-control'}),
            'address_city': TextInput(attrs={'class': 'form-control'}),
            'address_country': TextInput(attrs={'class': 'form-control'}),
        }
class CustomerUpdateForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'civility', 'last_name', 'first_name', 'email', 'phone', 'is_active',
            'address', 'address_num', 'address_box', 'address_zip_code', 'address_city', 'address_country'
        )
        # exclude = ('birthday','weight')
        widgets = {
            'civility': Select(attrs={'class': 'form-select'}),

            'last_name': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'is_active': Select(choices=TRUE_FALSE_CHOICES, attrs={'class': 'form-select'}),

            'address': TextInput(attrs={'class': 'form-control'}),
            'address_num': TextInput(attrs={'class': 'form-control'}),
            'address_box': TextInput(attrs={'class': 'form-control'}),
            'address_zip_code': TextInput(attrs={'class': 'form-control'}),
            'address_city': TextInput(attrs={'class': 'form-control'}),
            'address_country': TextInput(attrs={'class': 'form-control'}),
        }
class MuscleForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'style': 'width:50%'})
        }
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = ExoBody
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'style': 'width:50%'}),
            'muscle_group': Select(attrs={'class': 'form-select'}),
                   }
class HiitForm(forms.ModelForm):
    class Meta:
        model = ExoHiit
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'style': 'width:50%'}),
            'muscle_group': Select(attrs={'class': 'form-select'}),
        }