# Generated by Django 4.1.3 on 2022-11-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_taskfornewworker_data_of_execution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskfornewworker',
            name='status',
            field=models.CharField(choices=[('open', 'Нов'), ('in_progress', 'В прогрес'), ('pending', 'Очаква изпълнение'), ('partial_executed', 'Частично изпълненa'), ('close', 'Приключена')], default='Очаква изпълнение', max_length=50, verbose_name='Статус| State'),
        ),
        migrations.AlterField(
            model_name='taskfornewworker',
            name='vpn_from_work_laptop',
            field=models.CharField(choices=[('yes', 'да/yes'), ('no', 'не/no')], max_length=50, verbose_name='VPN от служебен лаптоп| VPN from work laptop'),
        ),
    ]
