# Generated by Django 2.0.2 on 2018-09-20 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0003_auto_20180920_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='go_live',
            name='name',
        ),
        migrations.DeleteModel(
            name='Go_Live',
        ),
    ]
