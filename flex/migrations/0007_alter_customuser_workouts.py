# Generated by Django 4.2 on 2023-04-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0006_alter_customuser_workouts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='workouts',
            field=models.ManyToManyField(to='flex.workout'),
        ),
    ]