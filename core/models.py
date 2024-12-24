from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]
STUDENT_STATUS_CHOICES = [
    ('Active', 'Active'),
    ('Graduated', 'Graduated'),
    ('Suspended', 'Suspended'),
]
ROLE_CHOICES = [
    ('Teacher', 'Teacher'),
    ('Administrator', 'Administrator'),
    ('Student', 'Student'),
]
SEMESTER_CHOICES = [
    ('First Semester', 'First Semester'),
    ('Second Semester', 'Second Semester'),
]


class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    admission_date = models.DateField()
    status = models.CharField(max_length=10, choices=STUDENT_STATUS_CHOICES)


class Course(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    credits = models.IntegerField()

    def __str__(self):
        return self.name
    

class AcademicRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='academic_records')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50, choices=SEMESTER_CHOICES)
    year = models.IntegerField()
    grade = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.student} - {self.course} ({self.semester} {self.year})'


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    hire_date = models.DateField()
    department = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.user.role})'
