from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('student/<int:student_id>/grades/', update_student_grades, name='update_student_grades'),

     # Student URLs
    path('students/', student_list, name='student_list'),
    path('students/<int:pk>/', student_detail, name='student_detail'),
    path('students/create/', student_create, name='student_create'),
    path('students/<int:pk>/edit/', student_update, name='student_update'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),

    # Staff URLs
    path('staff/', staff_list, name='staff_list'),
    path('staff/<int:pk>/', staff_detail, name='staff_detail'),
    path('staff/create/', staff_create, name='staff_create'),
    path('staff/<int:pk>/edit/', staff_update, name='staff_update'),
    path('staff/<int:pk>/delete/', staff_delete, name='staff_delete'),

    # Course URLs
    path('courses/', course_list, name='course_list'),
    path('courses/create/', course_create, name='course_create'),

    # Academic Record URLs
    path('records/', academic_record_list, name='academic_record_list'),
    path('records/create/', academic_record_create, name='academic_record_create'),
]
