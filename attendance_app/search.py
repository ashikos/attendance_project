from attendance_app.models import Attendance
import django_filters
from django_filters import rest_framework as filters


class AttendanceFilter(filters.FilterSet):
    date = filters.DateFilter('date')

    class Meta:
        model = Attendance
        fields = ['date']
