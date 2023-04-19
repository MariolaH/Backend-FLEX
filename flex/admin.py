from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(MuscleGroup)
admin.site.register(ExerciseList)
admin.site.register(Workout)


# Register your models here.
