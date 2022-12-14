# Generated by Django 4.1.3 on 2022-12-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_alter_taskfornewworker_is_new_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskfornewworker',
            name='access_to_read_write',
            field=models.CharField(blank=True, choices=[('read_only', 'без право да записва/without right to write'), ('write_read', 'може да прави записи /can write in directory')], max_length=12, null=True, verbose_name='Права само за четене-записване | Rights to read-write'),
        ),
        migrations.AlterField(
            model_name='taskfornewworker',
            name='status',
            field=models.CharField(choices=[('open', 'Нов'), ('in_progress', 'В прогрес'), ('pending', 'Очаква изпълнение'), ('partial_executed', 'Частично изпълненa'), ('close', 'Приключена')], default='pending', max_length=50, verbose_name='Статус| State'),
        ),
    ]
