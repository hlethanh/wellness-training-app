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
    path('customers/', views.customer_list, name='customers'),
    path('customers/create/', views.customer_create, name='customer-create'),
    path('customers/read/<int:id>/', views.customer_read, name='customer-read'),
    path('customers/update/<int:id>/', views.customer_update, name='customer-update'),
    path('customers/delete/<int:id>/', views.customer_delete, name='customer-delete'),

]
