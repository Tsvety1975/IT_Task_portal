from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import TextInput, EmailInput, forms

UserModel = get_user_model()

class CreateUserForm(auth_forms.UserCreationForm):
    error_messages = {
        "password_mismatch": ("Паролите не съвпадат."),

    }
    class Meta:
        model = UserModel
        fields = ("username","email","first_name","last_name","user_department", "phone_number","position")
        field_classes = {"username": auth_forms.UsernameField}



class EditUserForm(auth_forms.UserChangeForm):

    class Meta:
        model = UserModel
        fields = ("username", "email", "first_name", "last_name", "user_department", "phone_number","position")

        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'label': 'Име'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'label': 'Email'
            })
        }
        password = ReadOnlyPasswordHashField(
            label=("Password"),
            help_text=(
                "Raw passwords are not stored, so there is no way to see this "
                "user’s password, but you can change the password using "
                '<a href="{}">this form</a>.'
            ),
        )
