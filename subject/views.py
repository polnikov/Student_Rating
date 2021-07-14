from django.http.response import Http404
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views import generic

from .forms import SubjectForm
from .models import Subject


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
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects:add_subject')
    else:
        form = SubjectForm()
    return render(request, 'subject/add_subject.html', {'form': form})


class SubjectUpdateView(generic.UpdateView):
    model = Subject
    template_name = 'subject/update_subject.html'
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
    form_class = SubjectForm
    
    def get_object(self, queryset=None):

        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(id=pk)

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
