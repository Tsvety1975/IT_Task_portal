from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from IT_TaskPortal.team.models import Employees, Positions


# Register your models here.
@admin.register(Employees)
class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ['full_name']


@admin.register(Positions)
class PositionAdmin(ImportExportModelAdmin):
    list_display = ['position_name']