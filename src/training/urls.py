"""
URL configuration for training project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backoffice import views

urlpatterns = [
    path('model-blank/', views.model_blank, name='model-blank'),
    path('model-table/', views.model_table, name='model-table'),

    path('admin/', admin.site.urls),

    path('', views.index, name='home'),

    path('customer/', views.customer_list, name='customer-list'),
    path('customer/add/', views.customer_create, name='customer-create'),
    path('customer/show/<int:id>/', views.customer_read, name='customer-read'),
    path('customer/edit/<int:id>/', views.customer_update, name='customer-update'),
    path('customer/delete/<int:id>/', views.customer_delete, name='customer-delete'),

    path('muscle/', views.muscle_list, name='muscle-list'),
    path('muscle/add/', views.muscle_create, name='muscle-create'),
    path('muscle/edit/', views.muscle_update, name='muscle-update'),
    path('muscle/delete/<int:id>/', views.muscle_delete, name='muscle-delete'),

    path('exercise/', views.exercise_list, name='exercise-list'),
    path('exercise/add/', views.exercise_create, name='exercise-create'),
    path('exercise/edit/<int:id>/', views.exercise_update, name='exercise-update'),
    path('exercise/delete/<int:id>/', views.exercise_delete, name='exercise-delete'),

    path('hiit/', views.hiit_list, name='hiit-list'),
    path('hiit/add/', views.hiit_create, name='hiit-create'),
    path('hiit/edit/<int:id>/', views.hiit_update, name='hiit-update'),
    path('hiit/delete/<int:id>/', views.hiit_delete, name='hiit-delete'),
]
