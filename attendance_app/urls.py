from django.urls import path, include
from rest_framework import routers
from . import views
from attendance_app.models import CustomStudent

router = routers.DefaultRouter()
router.register('user', views.studentViewSet)
router.register('attendance', views.AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
