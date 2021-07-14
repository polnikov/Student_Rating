from django.urls import path

from . import views

app_name = 'subjects'
urlpatterns = [
    path('', views.subjects, name='subjects'),
    path('<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('<int:pk>/update', views.SubjectUpdateView.as_view(), name='update_subject'),
    path('addsubject', views.add_subject, name='add_subject'),
]
