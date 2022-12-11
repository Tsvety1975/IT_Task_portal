from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from IT_TaskPortal.accounts.forms import CreateUserForm, EditUserForm
from IT_TaskPortal.accounts.models import Department

UserModel = get_user_model()


# Register your models here.
@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    add_form = CreateUserForm
    form = EditUserForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email", "user_department", 'position',"phone_number",)}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ['first_name', 'last_name', 'email', 'user_department','phone_number']
    list_filter = ('first_name', 'last_name',)
    search_fields = ['last_name']


@admin.register(Department)
class DepartmentRegister(admin.ModelAdmin):
    list_display = ['department_name', 'short_department_name']