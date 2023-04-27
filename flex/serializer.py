
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser
from .models import *

class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = ['id', 'name']

class ExerciseListReadSerializer(serializers.ModelSerializer):
    muscles = MuscleGroupSerializer(many=True, required=False)
    class Meta:
        model = ExerciseList
        fields = ['id', 'name', 'muscles']

class ExerciseListWriteSerializer(serializers.ModelSerializer):
    muscles = MuscleGroupSerializer(many=True, required=False)
    class Meta:
        model = ExerciseList
        fields = ['id', 'name', 'muscles']

class WorkoutExerciseReadSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='exercise.name')
    id = serializers.ReadOnlyField(source='exercise.id')
    workout_exercise_id = serializers.ReadOnlyField(source='id')
    recorded_data = serializers.SerializerMethodField()
    # sets = serializers.Field(source='group.id')
    # name = serializers.Field(source='group.name')

    class Meta:
        model = WorkoutExercises
        fields = (
            'name',
            'id',
            # 'sets',
            # 'reps',
            # 'weight',
            'workout_exercise_id',
            'recorded_data'
        )
    
    def get_recorded_data(self, obj):
        qset = WorkoutExercises.objects.filter(workout=obj.workout, exercise=obj.exercise)
        return [{ "sets": e.sets,  "reps": e.reps, "weight": e.weight, "created_at": e.created_at } for e in qset]

class WorkoutExerciseWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercises
        fields = (
            'id',
            'exercise',
            'workout',
            'sets',
            'reps',
            'weight',
            'created_at',
        )

class WorkoutReadSerializer(serializers.ModelSerializer):
    # exercises = WorkoutExerciseReadSerializer(many=True, read_only=True)

    exercises = serializers.SerializerMethodField()
    class Meta:
        model = Workout
        fields = ['id', 'name', 'exercises']

    def get_exercises(self, obj):
        "obj is a Member instance. Returns list of dicts"""
        exercises = []
        exercise_ids = list(obj.exercises.all().values_list('id', flat=True))
        exercises_queryset = ExerciseList.objects.filter(id__in=exercise_ids).distinct()

        for exercise in exercises_queryset:
            recorded_data = []
            records = WorkoutExercises.objects.filter(workout=obj, exercise=exercise)
            for r in records:
                info = {
                    "sets": r.sets,
                    "reps": r.reps,
                    "weight": r.weight,
                    "created_at": r.created_at,
                }
                recorded_data.append(info)
            exercise_info = {
                "id": exercise.id,
                "name": exercise.name,
                "recorded_data": recorded_data,
            }
            exercises.append(exercise_info)
        return exercises


class WorkoutWriteSerializer(serializers.ModelSerializer):
    exercises = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=ExerciseList.objects.all())
    class Meta:
        model = Workout
        fields = ['id', 'name', 'exercises']

class CustomUserSerializer(serializers.ModelSerializer):
    # workouts = WorkoutWriteSerializer(many=True, required=False)
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
