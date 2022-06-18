from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, Teacher, Student
from django.db import transaction # used to make sure that all the changes are made in the databases

# User form for commoon details
class UserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit)
        if commit:
            user.is_active = True
            user.save()
        return user
    
# Teacher form for teacher details  
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('grades', 'subjects')
        
    @transaction.atomic 
    def save(self, commit=True):
        teacher = super().save(commit)
        if commit:
            teacher.save() # making sure the teacher data saves
        return teacher  
    
# Student form for student details
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('grade', 'age')
        
    @transaction.atomic
    def save(self, commit=True):
        student = super().save(commit)
        if commit:
            student.save() # making sure the student data saves
        return student

# You can add othe forms based on the two above 
# for other categories