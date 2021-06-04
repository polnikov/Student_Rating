from django.shortcuts import render

# Create your views here.

# from django.views.generic import CreateView
# from .models import Student

# class StudentCreateView(CreateView):
#       model = Student
#       fields = ('last_name', 'first_name')

from .models import Student

def index(request):
      return render(request, 'student/students.html')