from django.db import models
from django.urls import reverse


class Subject(models.Model):
    subject_name = models.CharField(
        verbose_name='Дисциплина',
        max_length=150,
        blank=False,
        unique=False,
    )
    FORMCONTROL = (
        (1, 'Экзамен'),
        (2, 'Диффзачет'),
        (3, 'Зачет'),
        (4, 'Курсовой проект'),
        (5, 'Курсовая работа'),
    )
    form_control = models.IntegerField(
        verbose_name='Форма контроля',
        choices=FORMCONTROL,
        blank=False,
        unique=False,
    )
    groups = models.ManyToManyField(
        'student.Group', 
        through='subject.GroupSubject', 
        verbose_name='Группы',
    )
    CATHEDRA = [
        # ('', ('------', '------')),
        ('ФИЭиГХ', (
            ('КВиЭ', 'водопользования и экологии'),
            ('КГЗиК', 'геодезии, землеустройства и кадастров'),
            ('КСФиХ', 'строительной физики и химии'),
            ('КТГВ', 'теплогазоснабжения и вентиляции'),
            ('КЭиЭ', 'электроэнергетики и электротехники'),
        )
        ),
        ('СФ', (
            ('КАДМиТ', 'автомобильных дорог, мостов и тоннелей'),
            ('КАСК', 'архитектурно-строительных конструкций'),
            ('КГЕО', 'геотехники'),
            ('КЖБК', 'железобетонных и каменных конструкций'),
            ('КИТ ', 'информационных технологий'),
            ('КМиДК', 'металлических и деревянных конструкций'),
            ('КМАТ', 'математики'),
            ('КОС', 'организации строительства'),
            ('КСМ', 'строительной механики'),
            ('КТСП', 'технологии строительного производства'),
            ('КТСМиМ', 'технологии строительных материалов и метрологии'),
        )
        ),
    ]
# TODO: добавить остальные факультеты и кафедры
    cathedra = models.CharField(
        verbose_name='Кафедра',
        max_length=100,
        choices=CATHEDRA,
        blank=False,
        unique=False,
    )
    teacher = models.CharField(
        verbose_name='Преподаватель',
        help_text='Фамилия И.О.',
        max_length=150,
        blank=True,
        unique=False,
    )
    att_date = models.DateField(
        verbose_name='Дата сдачи',
        auto_now=False,
        auto_now_add=False,
        unique=False,
        blank=True,
        null=True,
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
            'subject_name',
            '-att_date',
        ]
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return f'{self.subject_name} {dict(self.FORMCONTROL)[self.form_control]} {self.cathedra}'

    def get_absolute_url(self):
        """
        Возврат ссылки для доступа к деталям по конкретной дисциплине.
        """
        return reverse('subjects:subject_detail', args=[str(self.id)])

    @property
    def empty_att_date(self):
        if self.att_date == None:
            return 'Не назначена'
        else:
            return self.att_date

    @property
    def empty_teacher(self):
        if self.teacher == '':
            return 'Не назначен'
        else:
            return f'{self.teacher}'


class GroupSubject(models.Model):
    groups = models.ForeignKey(
        'student.Group', 
        on_delete=models.CASCADE,
        verbose_name='Группа',
    )
    subjects = models.ForeignKey(
        'subject.Subject', 
        on_delete=models.CASCADE, 
        verbose_name='Дисциплина',
    )
    SEMESTER = [
        (1, '1-1'), 
        (2, '1-2'), 
        (3, '2-3'), 
        (4, '2-4'), 
        (5, '3-5'), 
        (6, '3-6'), 
        (7, '4-7'), 
        (8, '4-8'), 
    ]
    semester = models.IntegerField(
        verbose_name='Семестр',
        choices=SEMESTER,
        blank=False,
    )


    class Meta:
        ordering = [
            'semester',
        ]
        verbose_name = 'Семестр'
        verbose_name_plural = 'Семестры'

    def __str__(self):
        return f'{self.semester}'
