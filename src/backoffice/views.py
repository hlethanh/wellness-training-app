from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from backoffice.models import *

def index(request):
    return render(request, 'backoffice/hello_world.html')
