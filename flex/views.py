from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import *
from .serializer import *

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class MuscleGroupViewSet(viewsets.ModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer

class ExerciseListViewSet(viewsets.ModelViewSet):
    queryset = ExerciseList.objects.all()
    # serializer_class = ExerciseListSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ExerciseListWriteSerializer
        return ExerciseListReadSerializer

    # def get_queryset(self):
    #     workout = self.request.workout
    #     if workout.is_authenticated:
    #         return ExerciseList.objects.filter(workout=workout)
    #     return ExerciseList.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(workout=self.request.workout)

    # def partial_update(self, request, pk=None):
    #     print(request.data)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return WorkoutWriteSerializer
        return WorkoutReadSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Workout.objects.filter(user=user)
        
        return Workout.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def partial_update(self, request, pk=None):
        print(request.data)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class WorkoutExercisesViewSet(viewsets.ModelViewSet):
    queryset = WorkoutExercises.objects.all()
    serializer_class = WorkoutExerciseWriteSerializer