import datetime
from datetime import timedelta

from dateutil import relativedelta
from django.db import models
from django.db.models import (DateField, DurationField, ExpressionWrapper, F,
                              Value)
from django.db.models.expressions import Case, Value, When
from django.db.models.fields import CharField
from django.urls import reverse
from django.utils.translation import gettext as _


class ExtendedStudentManager(models.Manager):

    def get_queryset(self):
        now = datetime.date.today()
        # d1 = datetime.date(self.start_date)
        # term = relativedelta.relativedelta(now, d1)
        return super().get_queryset().annotate(
            period=ExpressionWrapper(
                Value(now, DateField()) - F('start_date'),
                output_field=DurationField()
            )).annotate(
                semester=Case(
                    When(
                        period__lte=timedelta(days=153),
                        then=Value('1'),
                    ),
                    When(
                        period__gt=timedelta(days=153), period__lte=timedelta(days=365),
                        then=Value('2'),
                    ),
                    When(
                        period__gt=timedelta(days=365), period__lte=timedelta(days=518),
                        then=Value('3'),
                    ),
                    When(
                        period__gt=timedelta(days=518), period__lte=timedelta(days=731),
                        then=Value('4'),
                    ),
                    When(
                        period__gt=timedelta(days=731), period__lte=timedelta(days=884),
                        then=Value('5'),
                    ),
                    When(
                        period__gt=timedelta(days=884), period__lte=timedelta(days=1096),
                        then=Value('6'),
                    ),
                    When(
                        period__gt=timedelta(days=1096), period__lte=timedelta(days=1249),
                        then=Value('7'),
                    ),
                    When(
                        period__gt=timedelta(days=1249),
                        then=Value('8'),
                    ),
                    output_field=CharField(),
                ),
        )


class Student(models.Model):
    objects = models.Manager()
    extended = ExtendedStudentManager()
    
    student_id = models.IntegerField(
        verbose_name='Зачетная книжка',
        blank=False,
        unique=True,
        # validators=[validate_student_id]
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=30,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=30,
    )
    second_name = models.CharField(
        verbose_name='Отчество',
        max_length=30,
        blank=True,
        unique=False,
        default='',
    )
    BASIS = [
        ('Б', 'Бюджет'),
        ('К', 'Контракт'),
        ('ИГ', 'ИнГосЛиния'),
    ]
    basis = models.CharField(
        verbose_name='Основа обучения',
        max_length=20,
        choices=BASIS,
        default='Б',
        blank=False,
    )
    CITIZENSHIP = [
        ('РФ', 'Россия'),
        ('Ин', 'Иностранец'),
    ]
    citizenship = models.CharField(
        verbose_name='Гражданство',
        max_length=20,
        choices=CITIZENSHIP,
        default='РФ',
        blank=False,
    )
    LEVEL = [
        ('Бак', 'Бакалавриат'),
        ('Маг', 'Магистратура'),
    ]
    level = models.CharField(
        verbose_name='Уровень обучения',
        max_length=20,
        choices=LEVEL,
        blank=False,
    )
    group = models.ForeignKey(
        'student.Group', 
        on_delete=models.CASCADE, 
        related_name='students',
        verbose_name='Группа',
        )
    start_date = models.DateField(
        verbose_name='Дата зачисления',
        auto_now=False,
        auto_now_add=False,
    )
    STATUS = [
        ('ЯС', 'Является студентом'),
        ('АО', 'Академический отпуск'),
        ('ОТ', 'Отчислен'),
        ('Вк', 'Выпускник'),
    ]
    status = models.CharField(
        verbose_name='Текущий статус',
        max_length=30,
        choices=STATUS,
        default='ЯС',
        blank=False,
    )
    comment = models.CharField(
        verbose_name='Примечание',
        max_length=255,
        blank=True,
        unique=False,
        default='',
    )
    created_date = models.DateTimeField(
        verbose_name='Запись создана',
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        verbose_name='Запись обновлена',
        auto_now=True,
    )


    class Meta:
        ordering = [
            'group',
            'last_name',
            '-status',
        ]
        verbose_name = 'Обучающийся'
        verbose_name_plural = 'Обучающиеся'

    def __str__(self):
        # return f'{self.student_id}'
        return f'{self.last_name} {self.first_name} {self.second_name} / {self.student_id}'

    def get_absolute_url(self):
        """
        Возврат ссылки для доступа к деталям по конкретному студенту.
        """
        return reverse('students:student_detail', args=[str(self.student_id)])
    
    @property
    def fullname(self):
        return f'{self.last_name} {self.first_name} {self.second_name}'






    # @property
    # def period(self):
    #     d2 = datetime.now()
    #     d1 = self.start_date
    #     period = relativedelta.relativedelta(d2, d1)
    #     period = period.months + period.years * 12
    #     if self.status == 'ЯС':
    #         if self.level == 'Бак':
    #             if period < 46:
    #                 if period < 12:
    #                     if 0 <= period < 5:
    #                         return 1
    #                     else:
    #                         return 2
    #                 elif 12 <= period < 24:
    #                     if 12 <= period < 17:
    #                         return 3
    #                     else:
    #                         return 4
    #                 elif 24 <= period < 36:
    #                     if 24 <= period < 29:
    #                         return 5
    #                     else:
    #                         return 6
    #                 elif 36 <= period < 46:
    #                     if 36 <= period < 41:
    #                         return 7
    #                     else:
    #                         return 8
    #             else:
    #                 return 'Проверить'
    #         elif self.level == 'Маг':
    #             if period < 22:
    #                 if period < 12:
    #                     if 0 <= period < 5:
    #                         return 1
    #                     else:
    #                         return 2
    #                 elif 12 <= period < 22:
    #                     if 12 <= period < 17:
    #                         return 3
    #                     else:
    #                         return 4
    #             else:
    #                 return 'Проверить'
    #     else:
    #         return 'Проверить'

    #     def __str__(self):
    #         return f'{self.period}'

    # def clean_student_id(self):
    #     new_student_id = self.cleaned_data['student_id']
    #     if isinstance(new_student_id, int) is not True:
    #         raise forms.ValidationError({
    #             'student_id': 'номер введен некорректно'},
    #             code='invalid'
    #         )

        # if Student.objects.filter(student_id__iexact=self.student_id):
        #     raise forms.ValidationError({
        #         'student_id': f'номер {self.student_id} уже существует'},
        #         code='invalid'
        #     )
        # return new_student_id


class Group(models.Model):
    group_name = models.CharField(
        verbose_name='Группа',
        max_length=10,
        unique=True,
    )
    subjects = models.ManyToManyField(
        'subject.Subject',
        through='subject.GroupSubject', 
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f'{self.group_name}'


class Result(models.Model):
    MARK = (
        (1, '5'),
        (2, '4'),
        (3, '3'),
        (4, '2'),
        (5, 'зач'),
        (5, 'нз'),
        (6, 'ня'),
    )
    mark = models.CharField(
        verbose_name='Оценка',
        max_length=5,
        choices=MARK,
        blank=False,
        unique=False,
    )
    student = models.ManyToManyField(
        'student.Student',
        verbose_name='Обучающийся',
        related_name='results',
    )
    subject = models.ManyToManyField(
        'subject.Subject',
        verbose_name='Дисциплина',
    )

    class Meta:
            verbose_name = 'Оценка'
            verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'{self.mark}'
