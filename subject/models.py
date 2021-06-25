from django.db import models
from django.urls import reverse


class Subject(models.Model):
    subject_name = models.CharField(
        verbose_name='Наименование дисциплины',
        max_length=150,
        blank=False,
        unique=False,
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
        return f'{self.subject_name} {self.cathedra} {self.att_date}'

    def get_absolute_url(self):
        """
        Возврат ссылки для доступа к деталям по конкретной дисциплине.
        """
        return reverse('subject_detail', args=[str(self.id)])

    @property
    def empty_att_date(self):
        if self.att_date == None:
            return 'Не назначена'
        else:
            return f'{self.att_date}'

    @property
    def empty_teacher(self):
        if self.teacher == '':
            return 'Не назначен'
        else:
            return f'{self.teacher}'