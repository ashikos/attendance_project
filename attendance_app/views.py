from django.shortcuts import render
from rest_framework import viewsets
from attendance_app import serializers, models, search




# Create your views here.

class studentViewSet(viewsets.ModelViewSet):
    queryset = models.CustomStudent.objects.all()
    serializer_class = serializers.StudentSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer
    filterset_class = search.AttendanceFilter
