from django.urls import path
from . import views



urlpatterns = [
    path('', views.students, name='students'),
    path('addstudent', views.add_student, name='add_student'),
]

urlpatterns += [
    path('<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    
]