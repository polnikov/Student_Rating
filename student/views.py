from django.http import Http404
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views import generic
from django.views.generic import UpdateView
from django.views.generic.base import View

from .forms import StudentForm
from .models import Student


def students(request):
    """
    Функция отображения на сайте суммарной информации о студентах.
    """
    students_list = Student.extended.all().order_by('semester', 'group')
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
            'num_students': num_students,
            'num_basis_b': num_basis_b,
            'num_basis_k': num_basis_k,
            'num_basis_i': num_basis_i,
            'num_level_bak': num_level_bak,
            'num_level_mag': num_level_mag,
            'citizenship_ru': citizenship_ru,
            'citizenship_i': citizenship_i,
            'status_s': status_s,
            'status_ao': status_ao,
            'status_ot': status_ot,
            'students_list': students_list,
        },
    )


class StudentDetailView(generic.DetailView):
    model = Student
    queryset = Student.extended.all()

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


class StudentUpdateView(generic.UpdateView):
    model = Student
    template_name = 'student/update_student.html'
    # fields = [
    #         'last_name',
    #         'first_name',
    #         'second_name',
    #         'student_id',
    #         'citizenship',
    #         'basis',
    #         'level',
    #         'group',
    #         'start_date',
    #         'status',
    #         'comment',
    #     ]
    form_class = StudentForm
    
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
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:add_student')
    else:
        form = StudentForm()
    return render(request, 'student/add_student.html', {'form': form})


# def update_student(request, pk):
#     student = Student.objects.get(student_id=pk)
#     form = StudentForm(instance=student)
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('students:add_student')
    
#     context = {'form':form}
#     return render(request, 'student/update_student.html', context)
