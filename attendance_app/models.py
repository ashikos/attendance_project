from django.db import models
from django.contrib.auth.models import AbstractUser
from . import constants
import datetime


# Create your models here.


class CustomStudent(AbstractUser):
    """
    DETAILS OF STUDENT
        first_name : (char) first_name of user
        last_namne : (char) last_namne of user
        department  : (int) choice filed to know the department of student
        age : (int) age of user

    """
    department = models.IntegerField(choices=constants.DEPARTMENT_CHOICES)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Attendance(models.Model):
    """
    ATTENDANCE MARKING
        student : (fk) first_name of user
        date  : (date) date of which attendance is marking
        attendance : (int) to mark weather student is present or not

    """

    student = models.ForeignKey(CustomStudent, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    attendance = models.IntegerField(default=constants.present,
                                     choices=constants.ATTENDANCE_CHOICES)

