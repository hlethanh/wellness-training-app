from django.contrib import admin
from backoffice.models import *
from backoffice.widgets import PastCustomDatePickerWidget

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname','birthday', 'weight']
    formfield_overrides = {
        models.DateField:{'widget': PastCustomDatePickerWidget}
    }


admin.site.register(Customer, CustomerAdmin)