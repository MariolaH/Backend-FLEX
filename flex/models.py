from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class MuscleGroup(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

class ExerciseList(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    muscle = models.ManyToManyField('MuscleGroup')

    def __str__(self):
        return self.name


# Create your models here.
