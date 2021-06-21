from django.urls import path
from . import views



urlpatterns = [
    path('', views.subjects, name='subjects'),
    path('addsubject', views.add_subject, name='add_subject'),
]

urlpatterns += [
    path('<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
]