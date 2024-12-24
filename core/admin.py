from django.contrib import admin
from .models import CustomUser, Student, Course, AcademicRecord, Staff

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'first_name', 'last_name', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'role')
    list_filter = ('role', 'is_active', 'date_joined')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'registration_number', 'dob', 'gender', 'phone_number', 'status', 'admission_date')
    search_fields = ('user__username', 'registration_number', 'user__first_name', 'user__last_name', 'phone_number')
    list_filter = ('status', 'gender', 'admission_date')
    list_select_related = ('user',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'credits')
    search_fields = ('code', 'name')
    list_filter = ('credits',)

@admin.register(AcademicRecord)
class AcademicRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'semester', 'year', 'grade')
    search_fields = ('student__user__username', 'student__user__first_name', 'student__user__last_name', 'course__name')
    list_filter = ('semester', 'year', 'grade')
    list_select_related = ('student', 'course')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'hire_date', 'department')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone_number', 'department')
    list_filter = ('hire_date', 'department')
    list_select_related = ('user',)
