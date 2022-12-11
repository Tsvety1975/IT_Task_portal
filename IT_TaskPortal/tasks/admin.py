from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from IT_TaskPortal.tasks.models import TaskForNewWorker, Buildings, TelecomContract, ExternalTelekomTasks


# Register your models here.

@admin.register(Buildings)
class AdminBuildings(ImportExportModelAdmin):
    pass


@admin.register(TaskForNewWorker)
class AdminBTaskForNewUser(ImportExportModelAdmin):
    list_display = ['user', 'worker_last_name_bg', 'data_of_creation', 'status', ]
    list_filter = ('worker_department', 'worker_division',)
    search_fields = ['worker_last_name_bg', ]
    search_help_text = ['въведете фамилия на служителя, за когото се отнася заявката', ]



@admin.register(TelecomContract)
class AdminTelecomContracts(ImportExportModelAdmin):
    list_display = ['contractor_name', 'data_from','end_data_of_contract']
    list_filter =['data_from', 'end_data_of_contract',]
    search_fields = ['contractor_name',]
    search_help_text = ['въведете име на контрагент']


@admin.register(ExternalTelekomTasks)
class AdminExternalTelekomTasks(ImportExportModelAdmin):
    list_display = ['contractor_name', 'place_building']
    list_filter = ['data_of_creation', ]
    search_fields = ['contractor_name', ]
    search_help_text = ['въведете име на фирма']
