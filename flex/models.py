from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # workouts = models.ManyToManyField('Workout')

    def __str__(self):
        return self.username

class MuscleGroup(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

class ExerciseList(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    muscles = models.ManyToManyField('MuscleGroup')
    # sets = models.IntegerField(null=True, blank=True)
    # reps = models.IntegerField(null=True, blank=True)
    # weight = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    exercises = models.ManyToManyField('ExerciseList', through="WorkoutExercises")
    user = models.ForeignKey('CustomUser', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

class WorkoutExercises(models.Model):
    workout = models.ForeignKey('Workout', on_delete=models.PROTECT)
    exercise = models.ForeignKey('ExerciseList', on_delete=models.PROTECT)
    sets = models.IntegerField(null=True, blank=True, default=3)
    reps = models.IntegerField(null=True, blank=True, default=8)
    weight = models.IntegerField(null=True, blank=True, default=25)



# Create your models here.
