from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Student
from import_export import resources

class StudentResource(resources.ModelResource):

      class Meta:
            model = Student

class StudentAdmin(ImportExportModelAdmin):
      list_display = ('last_name', 'group', 'student_id', 'status', 'start_date', 'comment')
      list_filter = ('status', 'basis', 'group', 'citizenship', 'level')
      fields = [
      'student_id',
      ('last_name', 'first_name', 'second_name'),
      'citizenship', 'basis', 'level', 'group', 'start_date', 'status', 'comment',
      ]
      search_fields = ['last_name', 'student_id']
      resource_class = StudentResource
      list_editable = ['status', 'start_date', 'comment']

admin.site.register(Student, StudentAdmin)

