from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import Select, TextInput
from .models import Student


class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class StudentForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['level'].empty_label = 'Не выбрано'

    class Meta:
        model = Student
        fields = [
            'last_name',
            'first_name',
            'second_name',
            'student_id',
            'citizenship',
            'basis',
            'level',
            'group',
            'start_date',
            'status',
            'comment',
        ]
        widgets = {
            'last_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Фамилия',
                }),
            'first_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Имя',
                }),
            'second_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Отчество',
                }),
            'student_id': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер зачетной книжки',
                }),
            'citizenship': Select(
                attrs={
                    'class': 'form-control',
                }),
            'basis': Select(
                attrs={
                    'class': 'form-control',
                }),
            'level': Select(
                attrs={
                    'class': 'form-control',
                }),
            'group': Select(
                attrs={
                    'class': 'form-control',
                }),
            'start_date': MyDateInput(
                attrs={
                    'class': 'form-control',
                }),
            'status': Select(
                attrs={
                    'class': 'form-control',
                }),
            'comment': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Примечание',
                }),
        }

    def clean_student_id(self):
        student_id = self.cleaned_data['student_id']
        if isinstance(student_id, int) is not True:
            raise ValidationError('Номер зачетки введен некорректно')
        if Student.objects.filter(student_id__iexact=student_id):
            raise ValidationError(f'Номер {student_id} уже существует')
        return student_id


# class StudentForm(forms.Form):

#     last_name = forms.CharField(
#         max_length=30,
#         label="Please enter your email address",
#         widget=TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Фамилия',
#             })
#         )

#     first_name = forms.CharField(
#         max_length=30,
#         widget=TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Имя',
#             })
#         )

#     second_name = forms.CharField(
#         max_length=30,
#         widget=TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Отчество',
#             }),
#         required=False
#         )

#     student_id = forms.CharField(
#         max_length=10,
#         widget=TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Номер зачетной книжки',
#             })
#         )

#     citizenship = forms.ChoiceField(
#         choices=Student.CITIZENSHIP,
#         widget=Select(
#             attrs={
#                 'class': 'form-control',
#             })
#         )

#     # citizenship = forms.ChoiceField(
#     #     choices=Student.CITIZENSHIP,
#     #     widget=forms.RadioSelect(attrs={

#     #     })
#     #     )

#     basis = forms.ChoiceField(
#         choices=Student.BASIS,
#         initial=0,
#         widget=Select(
#             attrs={
#                 'class': 'form-control',
#             })
#         )

#     level = forms.ChoiceField(
#         choices=Student.LEVEL,
#         widget=Select(
#             attrs={
#                 'class': 'form-control',
#             })
#         )

#     group = forms.ChoiceField(
#         choices=Student.GROUP,
#         widget=Select(
#             attrs={
#                 'class': 'form-control',
#             })
#         )

#     start_date = forms.DateField(
#         widget=MyDateInput(
#             attrs={
#                 'class': 'form-control',
#             })
#     )

#     status = forms.ChoiceField(
#         choices=Student.STATUS,
#         widget=Select(
#             attrs={
#                 'class': 'form-control',
#             })
#         )

#     comment = forms.CharField(
#         max_length=255,
#         widget=TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Примечание',
#             }),
#         required=False
#         )


#     def save(self):
#         new_student = Student.objects.create(
#             student_id=self.cleaned_data['student_id'],
#             last_name=self.cleaned_data['last_name'],
#             first_name=self.cleaned_data['first_name'],
#             second_name=self.cleaned_data['second_name'],
#             basis=self.cleaned_data['basis'],
#             citizenship=self.cleaned_data['citizenship'],
#             level=self.cleaned_data['level'],
#             group=self.cleaned_data['group'],
#             start_date=self.cleaned_data['start_date'],
#             status=self.cleaned_data['status'],
#             comment=self.cleaned_data['comment'],
#         )
#         return new_student
