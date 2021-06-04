from django.db import models

# Create your models here.

class Student(models.Model):

      # student_id = models.AutoField(primary_key=False)
      student_id = models.CharField(verbose_name='Зачетная книжка', max_length=10, blank=False, unique=True)

      last_name = models.CharField(verbose_name='Фамилия', max_length=30)
      first_name = models.CharField(verbose_name='Имя', max_length=30)
      second_name = models.CharField(verbose_name='Отчество', max_length=30, blank=True)

      BASIS = (
          ('Б', 'Бюджет'),
          ('К', 'Контракт'),
          ('ИГ', 'ИнГосЛиния'),
      )

      basis = models.CharField(verbose_name='Основа обучения', max_length=20, choices=BASIS, blank=False)
      
      CITIZENSHIP = (
            ('РФ', 'Россия'),
            ('Ин', 'Иностранец'),
      )

      citizenship = models.CharField(verbose_name='Гражданство', max_length=20, choices=CITIZENSHIP, blank=False)

      LEVEL = (
            ('Бак', 'Бакалавриат'),
            ('Маг', 'Магистратура'),
      )

      level = models.CharField(verbose_name='Уровень обучения', max_length=20, choices=LEVEL, blank=False)

# добавить проверку по уровню
# если выбран Бак - то выбор таких групп
# если выбран Маг - то выбор таких групп
# если ничего не выбрано
 
      GROUP = (
            ('ТТ', 'ТТ'),
            ('ЭЭ', 'ЭЭ'),
            ('ИС', 'ИС'),
            ('ЗК', 'ЗК'),
            ('ТТм', 'ТТм'),
            ('ЗКм', 'ЗКм'),
            ('ЭЭм', 'ЭЭм'),
            ('ТГВм', 'ТГВм'),
            ('ВВм', 'ВВм'),
      )

      group = models.CharField(verbose_name='Группа', max_length=10, choices=GROUP)

      start_date = models.DateField(verbose_name='Дата зачисления', auto_now=False, auto_now_add=False)

      STATUS = (
            ('ЯС', 'Является студентом'),
            ('АО', 'Академический отпуск'),
            ('ОТ', 'Отчислен'),
      )
      
      status = models.CharField(verbose_name='Текущий статус', max_length=30, choices=STATUS, blank=False)

      comment = models.CharField(verbose_name='Примечание', max_length=255, blank=True)


      def __str__(self):
            return f'{self.last_name} {self.first_name} {self.second_name} {self.student_id}'

