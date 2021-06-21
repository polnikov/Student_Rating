from student.models import Student
from django.shortcuts import render

def main(request):
    groups = Student.objects.all().order_by('level', 'group')
    return render(request, 'main/main.html', 
                  context={'groups':groups})
