# Generated by Django 4.2 on 2023-04-18 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0003_exerciselist_musclegroup_exercise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musclegroup',
            name='exercise',
        ),
        migrations.AddField(
            model_name='exerciselist',
            name='muscle',
            field=models.ManyToManyField(to='flex.musclegroup'),
        ),
    ]
