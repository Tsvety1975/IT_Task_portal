# Generated by Django 4.1.3 on 2022-12-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_alter_taskfornewworker_adobe_software_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskfornewworker',
            name='worker_second_name_bg',
            field=models.CharField(default=' ', max_length=30, verbose_name='Бащино име кирилица| Second name'),
        ),
    ]
