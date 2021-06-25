# Generated by Django 3.2.4 on 2021-06-22 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ТТ', 'ТТ'), ('ЭЭ', 'ЭЭ'), ('ИС', 'ИС'), ('ЗК', 'ЗК'), ('ТТм', 'ТТм'), ('ЗКм', 'ЗКм'), ('ЭЭм', 'ЭЭм'), ('ТГВм', 'ТГВм'), ('ВВм', 'ВВм')], max_length=10, verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.group'),
        ),
    ]
