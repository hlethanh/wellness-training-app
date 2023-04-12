from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from backoffice.models import *

def model_blank(request):
    return render(request, 'backoffice/model_blank.html')
def model_table(request):
    return render(request, 'backoffice/model_table.html')
def customer_list(request):
    customers = Customer.objects.all()

    return render(request,
                  'backoffice/customer_list.html',
                  {'customers': customers})
def customer_detail(request, id):
    customer = Customer.objects.get(id=id)

    return render(request,
                  'backoffice/customer_detail.html',
                  {'customer': customer})