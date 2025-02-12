from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import password_validation, get_user_model
from django.utils.translation import gettext_lazy as _
from .models import Student, Staff, Course, AcademicRecord


User = get_user_model()

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control'
        }   
    ), help_text='Optional.')
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), help_text='Optional.')

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    is_owner = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label=_('Is farm equipment owner')  # Label for the checkbox
    )
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'username', 'email',
             'password1', 'password2',)
        

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'registration_number', 'dob', 'gender', 'phone_number', 'address', 'admission_date', 'status']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'phone_number', 'address', 'department']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'credits']

class AcademicRecordForm(forms.ModelForm):
    class Meta:
        model = AcademicRecord
        fields = ['student', 'course', 'semester', 'year', 'grade']
