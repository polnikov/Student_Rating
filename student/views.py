from django.shortcuts import redirect, render
from .models import Student
from django.http import Http404
from django.utils.translation import gettext as _
from .forms import StudentForm
from django.views import generic



def students(request):
    """
    Функция отображения на сайте суммарной информации о студентах.
    """
    students_list = Student.objects.all()
    
    num_records = Student.objects.all().count()
    
    num_basis_b = Student.objects.filter(basis__exact='Б').count()
    num_basis_k = Student.objects.filter(basis__exact='К').count()
    num_basis_i = Student.objects.filter(basis__exact='ИГ').count()
    num_level_bak = Student.objects.filter(level__exact='Бак').count()
    num_level_mag = Student.objects.filter(level__exact='Маг').count()
    citizenship_ru = Student.objects.filter(citizenship__exact='РФ').count()
    citizenship_i = Student.objects.filter(citizenship__exact='Ин').count()
    status_s = Student.objects.filter(status__exact='ЯС').count()
    status_ao = Student.objects.filter(status__exact='АО').count()
    status_ot = Student.objects.filter(status__exact='ОТ').count()
    
    num_students = num_records - status_ot
    
    # Отрисовка HTML-шаблона students.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'student/students.html',
        context={
            'num_students':num_students,
            'num_basis_b':num_basis_b,
            'num_basis_k':num_basis_k,
            'num_basis_i':num_basis_i,
            'num_level_bak':num_level_bak,
            'num_level_mag':num_level_mag,
            'citizenship_ru':citizenship_ru,
            'citizenship_i':citizenship_i,
            'status_s':status_s,
            'status_ao':status_ao,
            'status_ot':status_ot,
            'students_list':students_list,
            },
    )



class StudentDetailView(generic.DetailView):
    model = Student
    
    def get_object(self, queryset=None):
        
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(student_id=pk)

        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj



def add_student(request):
    bound_form = StudentForm(request.POST)
    if request.method == 'POST':
        if bound_form.is_valid():
            new_student = bound_form.save()
            return redirect('students')
        else:
            'Error'
    
    new_student = StudentForm()
    
    data = {
        'form':bound_form,
    }
    return render(request, 'student/add_student.html', data)




