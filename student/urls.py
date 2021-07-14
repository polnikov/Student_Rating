from django.urls import path

from . import views

app_name = 'students'
urlpatterns = [
    path('', views.students, name='students'), 
    path('<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'), 
    path('addstudent/', views.add_student, name='add_student'),
    path('<int:pk>/update', views.StudentUpdateView.as_view(), name='update_student'),
]
