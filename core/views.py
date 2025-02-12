from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Student, Staff, Course, AcademicRecord
from .forms import StudentForm, StaffForm, CourseForm, AcademicRecordForm

GRADE_POINTS = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 0
}

@login_required
def update_student_grades(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    records = AcademicRecord.objects.filter(student=student)

    if request.method == 'POST':
        for record in records:
            grade_key = f'grade_{record.id}'
            new_grade = request.POST.get(grade_key)
            if new_grade in GRADE_POINTS:  
                record.grade = new_grade
                record.save()
        return redirect('update_student_grades', student_id=student.id)

    cgpa = calculate_cgpa(records)
    
    return render(request, 'update_student_grades.html', {
        'student': student,
        'records': records,
        'cgpa': cgpa
    })

def calculate_cgpa(records):
    total_points = 0
    total_courses = 0

    for record in records:
        if record.grade in GRADE_POINTS:
            total_points += GRADE_POINTS[record.grade]
            total_courses += 1

    return round(total_points / total_courses, 2) if total_courses > 0 else 0.0

#student, staff, course, academic record

def home(request):
    return render(request, 'dashboard.html')

# Student Views
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

# Staff Views
@login_required
def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff_list.html', {'staff_members': staff_members})

@login_required
def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff_detail.html', {'staff': staff})

@login_required
def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff_form.html', {'form': form})

@login_required
def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff_form.html', {'form': form})

@login_required
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return render(request, 'staff_confirm_delete.html', {'staff': staff})

# Course Views
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})

# Academic Record Views
@login_required
def academic_record_list(request):
    records = AcademicRecord.objects.all()
    return render(request, 'academic_record_list.html', {'records': records})

@login_required
def academic_record_create(request):
    if request.method == 'POST':
        form = AcademicRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academic_record_list')
    else:
        form = AcademicRecordForm()
    return render(request, 'academic_record_form.html', {'form': form})
