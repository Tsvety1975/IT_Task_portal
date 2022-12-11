from  django.core import exceptions

def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Грешен формат за име')

def validate_only_digits(value):
    for ch in value:
        if not ch.isdigit():
            raise exceptions.ValidationError('Грешен формат за телефонен номер')