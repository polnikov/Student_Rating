from django.shortcuts import redirect, render
from .models import Subject
from django.utils.translation import gettext as _
from .forms import SubjectForm
from django.views import generic


def subjects(request):
    """
    Функция отображения на сайте суммарной информации о дисциплинах.
    """
    subjects_list = Subject.objects.all()
    num_subjects = Subject.objects.all().count()
    # Отрисовка HTML-шаблона Subjects.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'subject/subjects.html',
        context={
            'subjects_list':subjects_list,
            'num_subjects':num_subjects,
            },
    )


class SubjectDetailView(generic.DetailView):
    model = Subject


def add_subject(request):
    error_message = 'Форма пока не заполнена'
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects')
        else:
            error_message
    form = SubjectForm()
    
    data = {
        'form':form,
        'error_message':error_message,
    }
    return render(request, 'subject/add_subject.html', data)