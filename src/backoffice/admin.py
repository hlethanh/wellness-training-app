from django.contrib import admin
from backoffice.models import *
from backoffice.widgets import PastCustomDatePickerWidget

class CustomerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Customer._meta.fields]
    #list_display_links = ['username']
    formfield_overrides = {
        models.DateField:{'widget': PastCustomDatePickerWidget}
    }

class MuscleGroupExoStackedInline(admin.StackedInline):
    model = MuscleGroupExo
    extra = 0
    classes = ['no-collapse']
    #max_num = 2
    #show_change_link = True
    verbose_name = 'Exercise'
    verbose_name_plural = 'Exercises'
    ordering = ['id']
class MuscleGroupAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [MuscleGroupExoStackedInline]
    list_display = ['name','all_exercises']

    verbose_name = 'Hello'
    verbose_name_plural = 'Hellos'

    ordering = ['name']  # ASC

class MuscleGroupExoAdmin(admin.ModelAdmin):
    list_display = ['name','muscle_group']
    list_filter = ['muscle_group']
    search_fields = ['muscle_group__name']
    ordering = ['muscle_group__name']  # ASC


admin.site.register(Customer, CustomerAdmin)
admin.site.register(MuscleGroup,MuscleGroupAdmin)
admin.site.register(MuscleGroupExo, MuscleGroupExoAdmin)