
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser
from .models import *

class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = ['id', 'name']

class ExerciseListSerializer(serializers.ModelSerializer):
    muscles = MuscleGroupSerializer(many=True, required=False)
    class Meta:
        model = ExerciseList
        fields = ['id', 'name', 'muscles']

class WorkoutReadSerializer(serializers.ModelSerializer):
    exercises = ExerciseListSerializer(many=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'exercises']

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
