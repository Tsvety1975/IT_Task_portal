# Generated by Django 4.1.3 on 2022-12-12 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0024_alter_externaltelekomtasks_data_of_execution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externaltelekomtasks',
            name='place_building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.buildings', verbose_name='Сграда'),
        ),
    ]
