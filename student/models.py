from django.db import models
from django.urls import reverse

class Student(models.Model):

      student_id = models.CharField(verbose_name='Зачетная книжка',
                                    max_length=10,
                                    blank=False,
                                    unique=True)

      last_name = models.CharField(verbose_name='Фамилия',
                                   max_length=30)
      first_name = models.CharField(verbose_name='Имя',
                                    max_length=30)
      second_name = models.CharField(verbose_name='Отчество',
                                     max_length=30,
                                     blank=True,
                                     unique=False,
                                     default='')

      BASIS = [
          ('Б', 'Бюджет'),
          ('К', 'Контракт'),
          ('ИГ', 'ИнГосЛиния'),
      ]

      basis = models.CharField(verbose_name='Основа обучения', 
                               max_length=20, 
                               choices=BASIS,
                               default='Б', 
                               blank=False)
      
      CITIZENSHIP = [
            ('РФ', 'Россия'),
            ('Ин', 'Иностранец'),
      ]

      citizenship = models.CharField(verbose_name='Гражданство', 
                                     max_length=20, 
                                     choices=CITIZENSHIP,
                                     default='РФ', 
                                     blank=False)

      LEVEL = [
            ('Бак', 'Бакалавриат'),
            ('Маг', 'Магистратура'),
      ]

      level = models.CharField(verbose_name='Уровень обучения', 
                               max_length=20, 
                               choices=LEVEL, 
                               blank=False)

# TODO: добавить проверку по уровню
# TODO:  если выбран Бак - то выбор таких групп
# TODO:  если выбран Маг - то выбор таких групп
# TODO:  если ничего не выбрано
 
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

      group = models.CharField(verbose_name='Группа', 
                               max_length=10, 
                               choices=GROUP)

      start_date = models.DateField(verbose_name='Дата зачисления', 
                                    auto_now=False, 
                                    auto_now_add=False)

      STATUS = [
            ('ЯС', 'Является студентом'),
            ('АО', 'Академический отпуск'),
            ('ОТ', 'Отчислен'),
      ]
      
      status = models.CharField(verbose_name='Текущий статус', 
                                max_length=30, 
                                choices=STATUS, 
                                default='ЯС',
                                blank=False)

      comment = models.CharField(verbose_name='Примечание', 
                                 max_length=255, 
                                 blank=True,
                                 unique=False,
                                 default='')

      class Meta:
            ordering = ['last_name']
            verbose_name_plural = 'Обучающиеся'

      def __str__(self):
            return f'{self.last_name} {self.first_name} {self.second_name} {self.student_id}'
      
      def get_absolute_url(self):
            """
            Возврат ссылки для доступа к деталям по конкретному студенту.
            """
            return reverse('student_detail', args=[str(self.student_id)])
      
