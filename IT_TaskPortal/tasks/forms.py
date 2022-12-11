from django import forms

from IT_TaskPortal.tasks.models import TaskForNewWorker


class NewUserTaskCreateForm(forms.ModelForm):
    class Meta:
        model=TaskForNewWorker
        fields = '__all__'
        exclude = ('user', 'employee_responsible', 'remarks', 'status', 'data_of_creation', 'data_of_execution',)

        widgets = {
            'worker_from_data': forms.DateInput(
                attrs={
                    'type':'date',

                }),
            'worker_first_name_bg':forms.TextInput(
                attrs={
                    'class': "form-control",
                    'style': 'max-width: 500px;',
                }

            ),
        }

class EditTaskForNewUser(forms.ModelForm):
    class Meta:
        model = TaskForNewWorker
        fields = '__all__'
        readonly_fields = ('employee_responsible')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['employee_responsible'].disabled = True


