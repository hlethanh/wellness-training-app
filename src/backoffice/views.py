from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.forms import modelformset_factory, TextInput
#from django.template import loader
from backoffice.models import *
from backoffice.forms import CustomerCreateForm, CustomerUpdateForm, MuscleForm, ExerciseForm, HiitForm

#To use in the template
def simple_debug(obj):
    return obj.__dict__
def object_debug(obj):
    """
    How use:
        debug = object_debug(Customer.objects.filter(id=id))
        return debug
    """
    # import Modules for debug
    from django.http import JsonResponse
    from django.core.serializers import serialize
    import json

    serialized_data = serialize("json", obj)
    serialized_data = json.loads(serialized_data)
    serialized_data

    return JsonResponse(serialized_data, safe=False, status=200)


def model_blank(request):
    return render(request, 'backoffice/samples/model_blank.html')
def model_table(request):
    return render(request, 'backoffice/samples/model_table.html')
def index(request):
    return redirect('customer-list')


def customer_list(request):
    customers = Customer.objects.all().filter(is_superuser=False)

    return render(request,
                  'backoffice/customers/customer_list.html',
                  {'customers': customers})
def customer_create(request):
    if request.method == 'POST':
        form = CustomerCreate(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            #return redirect('program-detail', program.id)
            return redirect('customer-list')
    else:
        form = CustomerCreate()

    return render(request,
                  'backoffice/customers/customer_form.html',
                  {'form': form})
def customer_read(request, id):
    customer = Customer.objects.get(id=id)

    return render(request,
                  'backoffice/customers/customer_detail.html',
                  {'customer': customer})
def customer_update(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerUpdate(request.POST, instance=customer)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('customer-read', customer.id)
    else:
        form = CustomerUpdate(instance=customer)  # on pré-remplir le formulaire avec un groupe existant

    return render(request,
                  'backoffice/customers/customer_form.html',
                  {'form': form, 'customer': customer})
def customer_delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('customer-list')


def muscle_list(request):
    muscles = MuscleGroup.objects.all()

    return render(request,
                  'backoffice/muscles/muscle_list.html',
                  {'muscles': muscles})
def muscle_create(request):
    if request.method == 'POST':
        form = MuscleForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            customer = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            #return redirect('program-detail', program.id)
            return redirect('muscle-list')
    else:
        form = MuscleForm()

    return render(request,
                  'backoffice/muscles/muscle_add.html',
                  {'form': form})
def muscle_update(request):
    MusclesFormSet = modelformset_factory(MuscleGroup,
                                          fields=['name'],
                                          extra=0,
                                          widgets={'name': TextInput(attrs={'class':'form-control', 'style':'width:50%'})})
    if request.method == 'POST':

        muscles = MusclesFormSet(request.POST)

        if muscles.is_valid():

            instances = muscles.save(commit=False)

            for instance in instances:
                instance.save()

        return redirect('muscle-list')

    else:
        muscles = MusclesFormSet()

    # Add the formset to context dictionary
    context = {
        'muscles': muscles
    }

    return render(request,
                  'backoffice/muscles/muscle_update.html', context)
def muscle_delete(request, id):
    muscle = MuscleGroup.objects.get(id=id)
    muscle.delete()
    return redirect('muscle-list')

def exercise_list(request):
    exercises = Exercise.objects.all()

    return render(request,
                  'backoffice/exercises/exercise_list.html',
                  {'exercises': exercises})
def exercise_create(request):

    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            #return redirect('program-detail', program.id)
            return redirect('exercise-list')
    else:
        form = ExerciseForm()

    return render(request,
                  'backoffice/exercises/exercise_form.html',
                  {'form': form})
def exercise_update(request, id):

    exercise = Exercise.objects.get(id=id)

    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('exercise-list')
    else:
        form = ExerciseForm(instance=exercise)

    return render(request,
                  'backoffice/exercises/exercise_form.html',
                  {'form': form})
def exercise_delete(request, id):
    exercise = Exercise.objects.get(id=id)
    exercise.delete()
    return redirect('exercise-list')

def hiit_list(request):
    hiit = Hiit.objects.all()
    return render(request,
                  'backoffice/hiit/hiit_list.html',
                  {'hiit': hiit})
def hiit_create(request):

    if request.method == 'POST':
        form = HiitForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            #return redirect('program-detail', program.id)
            return redirect('hiit-list')
    else:
        form = HiitForm()

    return render(request,
                  'backoffice/hiit/hiit_add.html',
                  {'form': form})
def hiit_update(request, id):

    hiit = Hiit.objects.get(id=id)

    if request.method == 'POST':
        form = HiitForm(request.POST, instance=hiit)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('hiit-list')
    else:
        form = HiitForm(instance=hiit)

    return render(request,
                  'backoffice/hiit/hiit_update.html',
                  {'form': form})
def hiit_delete(request, id):
    hiit = Hiit.objects.get(id=id)
    hiit.delete()
    return redirect('hiit-list')
