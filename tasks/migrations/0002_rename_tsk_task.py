# Generated by Django 4.1.1 on 2022-09-25 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tsk',
            new_name='Task',
        ),
    ]
