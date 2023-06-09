# Generated by Django 4.2 on 2023-04-27 01:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0008_alter_workoutexercises_reps_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutexercises',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workoutexercises',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flex.exerciselist'),
        ),
        migrations.AlterField(
            model_name='workoutexercises',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flex.workout'),
        ),
    ]
