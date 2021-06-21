from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from dateutil import relativedelta


class Student(models.Model):

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

      # TODO: добавить проверку групп по уровню

      GROUP = [
            ('ТТ', 'ТТ'),
            ('ЭЭ', 'ЭЭ'),
            ('ИС', 'ИС'),
            ('ЗК', 'ЗК'),
            ('ТТм', 'ТТм'),
            ('ЗКм', 'ЗКм'),
            ('ЭЭм', 'ЭЭм'),
            ('ТГВм', 'ТГВм'),
            ('ВВм', 'ВВм'),
      ]
      
      group = models.CharField(
            verbose_name='Группа', 
            max_length=10, 
            choices=GROUP,
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
      
      # class CourseManager(models.Manager):
      #       def get_queryset(self):
      #             d2 = datetime.now()
      #             d1 = self.start_date
      #             term = relativedelta.relativedelta(d2, d1)
      #             term = term.months + term.years * 12
      #                   return super().get_queryset().annotate(
      #                         course=Case(
      #                               When(
      #                                     term__lt=12,
      #                                     then=Value(1),
      #                               ),
      #                               When(
                                          
      #                               )
      #                         )
      #                   )



      @property
      def fullname(self):
            return f'{self.last_name} {self.first_name} {self.second_name}'



      @property
      def course(self):
            d2 = datetime.now()
            d1 = self.start_date
            term = relativedelta.relativedelta(d2, d1)
            term = term.months + term.years * 12
            if self.status == 'ЯС':
                  if self.level == 'Бак':
                        if term < 46:
                              if term < 12:
                                    return 1
                              elif 12 <= term < 24:
                                    return 2
                              elif 24 <= term < 36:
                                    return 3
                              elif 36 <= term < 46:
                                    return 4
                        else:
                              return 'Проверить'
                  elif self.level == 'Маг':
                        if term < 22:
                              if term < 12:
                                    return 1
                              elif 12 <= term < 22:
                                    return 2
                        else:
                              return 'Проверить'
            else:
                  return 'Проверить'
            
            def __str__(self):
                  return self.course



      class Meta:
            ordering = [
                  'last_name', 
                  'first_name', 
                  'second_name', 
                  'status',
                  ]
            verbose_name = 'Обучающийся'
            verbose_name_plural = 'Обучающиеся'



      def __str__(self):
            return f'{self.group}'
            # return f'{self.last_name} {self.first_name} {self.second_name} / {self.student_id}'



      def get_absolute_url(self):
            """
            Возврат ссылки для доступа к деталям по конкретному студенту.
            """
            return reverse('student_detail', args=[str(self.student_id)])



      def clean_student_id(self):
            new_student_id = self.cleaned_data['student_id']
            if isinstance(new_student_id, int) is not True:
                  raise forms.ValidationError({
                        'student_id': 'номер введен некорректно'}, 
                        code='invalid'
                  )
                        
            if Student.objects.filter(student_id__iexact=self.student_id):
                  raise forms.ValidationError({
                        'student_id': f'номер {self.student_id} уже существует'}, 
                        code='invalid'
                  )
                  
            return new_student_id
