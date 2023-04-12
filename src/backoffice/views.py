from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from backoffice.models import *
from backoffice.forms import CustomerForm

def model_blank(request):
    return render(request, 'backoffice/model_blank.html')
def model_table(request):
    return render(request, 'backoffice/model_table.html')
def customer_list(request):
    customers = Customer.objects.all()

    return render(request,
                  'backoffice/customer_list.html',
                  {'customers': customers})
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            customer = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            #return redirect('program-detail', program.id)
            return redirect('customers')
    else:
        form = CustomerForm()

    return render(request,
                  'backoffice/customer_create.html',
                  {'form': form})
def customer_detail(request, id):
    customer = Customer.objects.get(id=id)

    return render(request,
                  'backoffice/customer_detail.html',
                  {'customer': customer})
def customer_update(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('customer-detail', customer.id)
    else:
        form = CustomerForm(instance=customer)  # on pré-remplir le formulaire avec un groupe existant

    return render(request,
                  'backoffice/customer_update.html',
                  {'form': form})