from django.db import models
from django.contrib.auth import models as auth_models
from django.core import validators

from IT_TaskPortal.accounts.validators import validate_only_letters, validate_only_digits


# Create your models here.

class Department(models.Model):
    department_name = models.CharField(
        max_length=50,

    )
    short_department_name =models.CharField(
        max_length=10,
    )
    def __str__(self):
        return f'{self.short_department_name}'

class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,

        blank=False,
        null=False,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,


    ),
        verbose_name="Име | First name"
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
    ),
        verbose_name='Фамилия | Family name'
    )
    email=models.EmailField(blank=False, null=False, unique=True, verbose_name="E-Mail")

    phone_number = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=(
            validate_only_digits,
            validators.MinLengthValidator(9)
    ),verbose_name='Мобилен/служебен номер | Mobile/work phone number',
    )

    user_department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
        related_name='shor',
        null=True,
        verbose_name='Дирекция  | Department',)

    position = models.CharField(
        null=True,
        blank=True,
        max_length=40,
        verbose_name='Длъжност | Position',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


