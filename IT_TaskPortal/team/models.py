from django.db import models

# Create your models here.

from django.core import validators
from django.db import models


# Create your models here.

class Positions(models.Model):
    position_name = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return self.position_name


class Employees(models.Model):
    first_name = models.CharField(
        max_length=15,
    )

    last_name = models.CharField(
        max_length=15,
    )

    employee_position = models.ForeignKey(
        Positions,
        on_delete=models.RESTRICT
    )

    employee_email = models.EmailField()

    employee_dekt = models.CharField(
        max_length=4,
        validators=(
            validators.MinLengthValidator(4, 'Невалиден формат'),
        ),
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
