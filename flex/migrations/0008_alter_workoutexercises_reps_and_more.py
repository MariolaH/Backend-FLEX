# Generated by Django 4.2 on 2023-04-26 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0007_alter_workoutexercises_reps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutexercises',
            name='reps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workoutexercises',
            name='sets',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workoutexercises',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
