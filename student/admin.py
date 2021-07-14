from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Group, Result, Student

admin.site.site_header = 'Рейтинг ФИЭиГХ'


class SemesterFilter(admin.SimpleListFilter):
    title = 'Семестр'
    parameter_name = 'semester'

    def lookups(self, request, model_admin):
        return (
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            ('Проверить', 'Проверить'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(semester=value).exclude(status='ОТ')
        else:
            return queryset


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = [
            'student_id', 
            'last_name', 
            'first_name', 
            'second_name',
            'group', 
            'basis', 
            'citizenship', 
            'level', 
            'start_date', 
            'status', 
            'comment', 
            ]
        # exclude = [
        #     'created_date', 
        #     'updated_date', 
        #     ]
        import_id_fields = ('student_id',)


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = (
        'last_name',
        'fullname',
        'student_id',
        'group',
        'semester',
        'status',
        'start_date',
        'comment',
        'updated_date',
        'created_date',
    )
    list_filter = (
        'status',
        'level',
        SemesterFilter,
        'basis',
        'citizenship',
    )
    fields = [
        'student_id',
        ('last_name', 'first_name', 'second_name'),
        'citizenship',
        'basis',
        'level',
        'group',
        'start_date',
        'status',
        'comment',
    ]
    search_fields = [
        'last_name',
        'student_id',
        'semester',
        'fullname',
    ]
    resource_class = StudentResource
    list_editable = [
        'comment',
        'status',
        'start_date',
    ]
    ordering = [
        'level',
        '-status',
        'last_name',
    ]

    
    def get_queryset(self, request):
        return self.model.extended.all()
    
    def semester(self, obj):
        return obj.semester
    
    semester.short_description = 'Семестр'
    semester.admin_order_field = 'semester'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = [
        'group_name',
    ]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    fields = [
        'student',
        'subject',
        'mark',
    ]
