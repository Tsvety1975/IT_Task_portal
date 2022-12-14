# Generated by Django 4.1.3 on 2022-12-02 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_remove_taskfornewworker_access_to_read_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskfornewworker',
            name='color_copy_possibility',
            field=models.BooleanField(blank=True, null=True, verbose_name='Цветно копиране| Color copy'),
        ),
        migrations.AlterField(
            model_name='taskfornewworker',
            name='color_printing_possibility',
            field=models.BooleanField(verbose_name='Цветно отпечатване| Color print'),
        ),
    ]
