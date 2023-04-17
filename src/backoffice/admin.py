from django.contrib import admin
from backoffice.models import *
from backoffice.widgets import PastCustomDatePickerWidget

class CustomerAdmin(admin.ModelAdmin):
    fields = ['last_name',
              'first_name',
              'username',
              'email',
              'phone',
              'address',
              'address_num',
              'address_box',
              'address_zip_code',
              'address_city',
              'address_country',
              'is_active',
              'is_staff',
              'is_superuser',
              'date_joined',
              'last_login',
              'groups',
              'user_permissions',
              ]

    #list_display = [f.name for f in Customer._meta.fields]
    list_display = ['civility',
                    'last_name',
                    'first_name',
                    'username',
                    'email',
                    'phone',
                    'address',
                    'address_num',
                    'address_box',
                    'address_zip_code',
                    'address_city',
                    'address_country',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    ]
    list_display_links = ['email']

    list_filter = ['is_active','is_staff', 'is_superuser']

    search_fields = ['last_name', 'first_name']

    formfield_overrides = {
        models.DateField:{'widget': PastCustomDatePickerWidget}
    }
class ExerciseStackedInline(admin.StackedInline):
    model = Exercise
    extra = 0
    classes = ['no-collapse']
    #max_num = 2
    #show_change_link = True
    verbose_name = 'Exercise'
    verbose_name_plural = 'Exercises'
    ordering = ['id']
class MuscleGroupAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [ExerciseStackedInline]
    list_display = ['name','exercises']
    ordering = ['name']  # ASC
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name','muscle_group']
    list_filter = ['muscle_group']
    search_fields = ['muscle_group__name']
    ordering = ['muscle_group__name']  # ASC
class HiitAdmin(admin.ModelAdmin):
    list_display = ['name', 'muscle_group']
    list_filter = ['muscle_group']
    search_fields = ['muscle_group__name']
    ordering = ['name']  # ASC


admin.site.register(Customer, CustomerAdmin)
admin.site.register(MuscleGroup,MuscleGroupAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Hiit, HiitAdmin)