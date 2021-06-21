from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Subject
from import_export import resources

class SubjectResource(resources.ModelResource):

      class Meta:
            model = Subject
            import_fields = (
                  'cathedra', 
                  'subject_name', 
                  'teacher', 
                  'att_date', 
                  'comment')
            fields = (
                  'id', 
                  'cathedra', 
                  'subject_name', 
                  'teacher', 'att_date', 
                  'comment',
                  )

class SubjectAdmin(ImportExportModelAdmin):
      list_display = (
            'subject_name', 
            'cathedra', 
            'teacher', 
            'att_date', 
            'comment', 
            'updated_date', 
            'created_date',
            )
      
      list_filter = (
            'cathedra', 
            'teacher', 
            'att_date',
            )
      
      fields = [
      ('subject_name', 'cathedra', 'teacher'),
      'att_date', 
      'comment',
      ]
      
      search_fields = [
            'teacher', 
            'cathedra', 
            'att_date',
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

admin.site.register(Subject, SubjectAdmin)

