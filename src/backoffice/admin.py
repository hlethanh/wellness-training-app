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
    model = ExoBody
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

class ExoHiitAdmin(admin.ModelAdmin):
    list_display = ['name', 'muscle_group']
    list_filter = ['muscle_group']
    search_fields = ['muscle_group__name']
    ordering = ['name']  # ASC
class FormHiitAdmin(admin.ModelAdmin):
    list_display = ['exo_hiit', 'set']
class TrainingHiit(admin.TabularInline):
    model = FormHiit
    extra = 0
    classes = ['no-collapse']
    verbose_name = 'Training'
    verbose_name_plural = 'Training'
    ordering = ['id']
class ProgramHiitAdmin(admin.ModelAdmin):
    list_display = ['title', 'customer', 'level']
    inlines = [TrainingHiit]
    readonly_fields = ['program_type']

class ExoBodyAdmin(admin.ModelAdmin):
    list_display = ['name','muscle_group']
    list_filter = ['muscle_group']
    search_fields = ['muscle_group__name']
    ordering = ['muscle_group__name']  # ASC
class FormBodyAdmin(admin.ModelAdmin):
    list_display = ['exo_body','set','rep','pause','type']
    fields = ['program_body','exo_body','type', 'set','rep','pause']
class TrainingBody(admin.TabularInline):
    model = FormBody
    extra = 0
    classes = ['no-collapse']
    verbose_name = 'Training'
    verbose_name_plural = 'Training'
    ordering = ['id']
class ProgramBodyAdmin(admin.ModelAdmin):
    list_display = ['title', 'customer']
    inlines = [TrainingBody]
    readonly_fields = ['program_type']

class ProgramMixteAdmin(admin.ModelAdmin):
    list_display = ['title', 'customer']
    readonly_fields = ['program_type']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(MuscleGroup,MuscleGroupAdmin)

admin.site.register(ExoHiit, ExoHiitAdmin)
admin.site.register(FormHiit, FormHiitAdmin)
admin.site.register(ProgramHiit, ProgramHiitAdmin)

admin.site.register(ExoBody, ExoBodyAdmin)
admin.site.register(FormBody, FormBodyAdmin)
admin.site.register(ProgramBody, ProgramBodyAdmin)

admin.site.register(ProgramMixte, ProgramMixteAdmin)

admin.site.register(PType)

