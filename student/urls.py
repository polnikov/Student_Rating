from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('', views.students, name='students'),
]

urlpatterns += [
    path('<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
]