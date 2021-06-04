from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.

from .models import Student

# admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
      list_display = ('last_name', 'first_name', 'second_name', 'group', 'student_id')
      list_filter = ('status', 'basis', 'citizenship', 'level')
      fields = ['student_id',
      ('last_name', 'first_name', 'second_name'),
      'citizenship', 'basis', 'level', 'group', 'start_date', 'status', 'comment',
      ]


admin.site.register(Student, StudentAdmin)
