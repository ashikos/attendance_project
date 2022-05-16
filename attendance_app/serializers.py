from django.db.models import Count
from rest_framework import serializers
from attendance_app import models ,constants
import datetime


class StudentSerializer(serializers.ModelSerializer):

    days_present = serializers.SerializerMethodField('no_of_days_present')
    days_absent = serializers.SerializerMethodField('no_of_days_absent')

    def no_of_days_present(self, obj):
        """
        serializer method field to fetch no of days attended by student
        """
        count = models.Attendance.objects.filter(
            attendance=constants.present,student=obj.id).count()
        return count

    def no_of_days_absent(self, obj):
        """
        serializer method field to fetch no of days absent by student
        """
        count = models.Attendance.objects.filter(
            attendance=constants.absent,student=obj.id).count()
        return count

    def create(self, validated_data):
        """ To add username using firstname and lastname """
        username = validated_data['first_name'] + validated_data['last_name']
        validated_data['username'] = username
        super().create(validated_data)
        return validated_data

    class Meta:
        model = models.CustomStudent
        fields = ['id', 'first_name', 'last_name', 'department', 'age',
                  'days_present','days_absent']


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Attendance
        fields = ['id', 'student', 'date', 'attendance', ]

    def create(self, validated_data):
        """
        Checking whether attendance already marked for a particular date
        """
        if models.Attendance.objects.filter(
                date=validated_data['date'],student=validated_data['student']).exists():
            raise serializers.ValidationError(
                'attendance already registered     ')
        super().create(validated_data)

        return validated_data
