from django.contrib import admin
from django.db.models.expressions import ExpressionWrapper, F, Value
from django.db.models.fields import DateTimeField, DurationField
from import_export.admin import ImportExportModelAdmin
from .models import Student
from import_export import resources
from dateutil import relativedelta
from django.utils import timezone
from datetime import datetime, timedelta


class StudentResource(resources.ModelResource):

      class Meta:
            model = Student
            
            exclude = ['id']
            
            import_id_fields = ('student_id')

# class CourseFilter(admin.SimpleListFilter):
#       title = 'Курс'
#       parameter_name = 'course'
      
#       def lookups(self, request, model_admin):
#           return (
#                 (1, 1),
#                 (2, 2),
#                 (3, 3),
#                 (4, 4),
#                 ('Проверить', 'Проверить'),
#           )
      
      # def queryset(self, request, queryset):
      #       value = self.value()
      #       now = timezone.now()
      #       queryset = queryset.annotate(
      #             term=ExpressionWrapper(
      #           Value(now, DateTimeField()) - F('start_date'),
      #           output_field=DurationField()
      #           ))
            
      #       if value == 1:
      #             return queryset.filter(term__lte=timedelta(days=365))
      #       elif value == 2:
      #             return queryset.filter(term__gt=timedelta(days=365), term__lte=timedelta(days=365 * 2))
      #       elif value == 3:
      #             return queryset.filter(term__gt=timedelta(days=365 * 2), term__lte=timedelta(days=365 * 3))
      #       elif value == 4:
      #             return queryset.filter(term__gt=timedelta(days=365 * 3))
      #       return queryset
      
      
      # def queryset(self, request, queryset):
      #       value = self.value()
      #       d2 = datetime.now()
      #       d1 = Student.start_date
      #       term = relativedelta.relativedelta(d2, d1)
      #       term = term.months + term.years * 12
      #       queryset = queryset.annotate(
      #             term=ExpressionWrapper(
      #           output_field=DurationField()
      #           ))
            
      #       if value == 1:
      #             return queryset.filter(term__lt=12)
      #       elif value == 2:
      #             return queryset.filter(term__gte=12, term__lt=24)
      #       elif value == 3:
      #             return queryset.filter(term__gte=24, term__lt=36)
      #       elif value == 4:
      #             return queryset.filter(term__gte=34, term__lt=46)
            
            
      #       # print(list(queryset.values_list('days', flat=True)))
      #       return queryset


class StudentAdmin(ImportExportModelAdmin):
      
      list_display = (
            'last_name', 
            'student_id', 
            'group', 
            'course', 
            'status', 
            'start_date', 
            'comment', 
            'updated_date', 
            'created_date',
            )
      
      list_filter = (
            'status', 
            'level', 
            'group', 
            # CourseFilter,
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
            'student_id'
            ]
      
      resource_class = StudentResource
      
      list_editable = [
            'comment', 
            'status',
            ]
      
      ordering = [
            'level', 
            '-status', 
            'last_name',
            ]


            # if value == 1:
            #       return queryset.filter(course=1)
            
            # d2 = datetime.now()
            # d1 = self.start_date
            # term = relativedelta.relativedelta(d2, d1)
            # term = term.months + term.years * 12
            # if self.status == 'ЯС':
            #       if self.level == 'Бак':
            #             if term < 46:
            #                   if term < 12:
            #                         return '1'
            #                   elif 12 <= term < 24:
            #                         return '2'
            #                   elif 24 <= term < 36:
            #                         return '3'
            #                   elif 36 <= term < 46:
            #                         return '4'
            #             else:
            #                   return 'Проверить'
            #       elif self.level == 'Маг':
            #             if term < 22:
            #                   if term < 12:
            #                         return '1'
            #                   elif 12 <= term < 22:
            #                         return '2'
            #             else:
            #                   return 'Проверить'
            # else:
            #       return 'Проверить'
            # return queryset





admin.site.register(Student, StudentAdmin)