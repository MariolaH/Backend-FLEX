from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import *
# from flex import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'musclegroup', MuscleGroupViewSet)
router.register(r'exerciselist', ExerciseListViewSet)
router.register(r'workout', WorkoutViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


