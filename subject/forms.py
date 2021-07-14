from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms.widgets import DateInput, Select, TextInput

from .models import Subject


class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = [
            'subject_name',
            'cathedra',
            'teacher',
            'form_control',
            'att_date',
            'comment',
        ]
        widgets = {
            'subject_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Полное наименование дисциплины',
            }),
            'cathedra': Select(attrs={
                'class': 'form-control',
            }),
            'teacher': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия И.О. преподавателя',
            }),
            'form_control': Select(attrs={
                'class': 'form-control',
            }),
            'att_date': DateInput(attrs={
                'class': 'form-control',
            }, format='%d.%m.%Y',),

            'comment': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Примечание',
            }),
        }


# class SubjectForm(forms.Form):

#     subject_name = forms.CharField(
#         max_length=150,
#         widget=TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Полное наименование дисциплины',
#             })
#         )

#     cathedra = forms.ChoiceField(
#         choices=Subject.CATHEDRA,
#         initial={'cathedra': 'sfsfsf'},
#         widget=Select(
#             attrs={
#                 'class': 'form-control',
#             })
#         )

#     teacher = forms.CharField(
#         max_length=150,
#         widget=TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Фамилия И.О. преподавателя',
#             }),
#         required=False
#         )

#     att_date = forms.DateField(
#         widget=MyDateInput(
#             attrs={
#                 'class': 'form-control',
#             }),
#         required=False
#     )

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
#         new_subject = Subject.objects.create(
#             subject_name=self.cleaned_data['subject_name'],
#             cathedra=self.cleaned_data['cathedra'],
#             teacher=self.cleaned_data['teacher'],
#             att_date=self.cleaned_data['att_date'],
#             comment=self.cleaned_data['comment'],
#         )
#         return new_subject
