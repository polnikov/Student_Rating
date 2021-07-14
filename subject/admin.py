from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import GroupSubject, Subject


class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject
        # import_fields = (
        #     'cathedra',
        #     'subject_name',
        #     'teacher',
        #     'att_date',
        #     'comment')
        # fields = (
        #     # 'id',
        #     'cathedra',
        #     'subject_name',
        #     'teacher', 'att_date',
        #     'comment',
        # )
        exclude = [
            'id', 
            ]
        # import_id_fields = ('subject_name')

@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    list_display = (
        'subject_name',
        'cathedra',
        'teacher',
        'form_control',
        'att_date',
        'comment',
        'updated_date',
        'created_date',
    )
    list_filter = (
        'subject_name',
        'cathedra',
        'teacher',
        'form_control',
        'att_date',
    )
    fields = [
        ('subject_name', 'cathedra', 'teacher'),
        'form_control',
        'att_date',
        'comment',
    ]
    search_fields = [
        'subject_name',
        'teacher',
        'cathedra',
        'att_date',
        'form_control',
    ]
    resource_class = SubjectResource
    list_editable = [
        'att_date',
        'comment',
    ]
    ordering = [
        'cathedra',
        'subject_name',
        '-att_date',
    ]

@admin.register(GroupSubject)
class GroupSubjectAdmin(admin.ModelAdmin):
    fields = [
        'semester',
        'groups', 
        'subjects', 
    ]
