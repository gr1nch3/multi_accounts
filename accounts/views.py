from django.http import JsonResponse
from django.shortcuts import redirect, render
from accounts.forms import UserForm, TeacherForm, StudentForm
from accounts.models import User, Teacher, Student
from django.views.generic.detail import DetailView

from django.contrib.auth import login

# Create your views here.
# Using Function based views

""" 
    You could get creative with the views, but since we will have to use two models 
    to represent the data of a single user with the only distinction being the role,
    we can use the user and teacher or student model in a single function on a single page or template
    to get the data needed the forms created will take care of the rest.
    
    ### also we'll need crispy forms to make the forms look nice and support the two forms one template
    
    or you could create different view functions for each role, which will then presented on different 
    pages or template on the signup form, and with this method you could use class based views then and
    get all the benefits of it, but that would be a lot of views. 
"""
    
# function with multi forms to create a new teacher
def createTeacher(request):
    userform = UserForm()
    teacherform = TeacherForm()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        teacherform = TeacherForm(request.POST)
        if userform.is_valid() and teacherform.is_valid():
            uf = userform.save(commit=False)
            uf.save()
            tf = teacherform.save(commit=False)
            tf.user = uf # set the user to the teacher form user_id
            uf.role = 2 # set the role to 2 for teacher in the user table
            tf.save()
            uf.save()
            
            #Login the user and redirect to the home page
            if uf is not None:
                if uf.is_active:
                    login(request, uf) # login the user
                    return redirect('accounts:home') # redirect to the home page
            
        else:
            # used dictionary to know the field and the error
            errors = {} # create a dictionary to store the errors
            # loop through the form fields and add the errors to the dictionary
            for field in userform or teacherform:
                for error in field.errors:
                    errors[field.name] = error # add the error to the dictionary
            return JsonResponse({"status": False, "errors": errors})
                    
    else:
        userform = UserForm()
        teacherform = TeacherForm()
    return render(request, 'accounts/createTeacher.html', {'userform': userform, 'teacherform': teacherform})

# function with multi forms to create a new student
def createStudent(request):
    userform = UserForm()
    studentform = StudentForm()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        studentform = StudentForm(request.POST)
        if userform.is_valid() and studentform.is_valid():
            uf = userform.save(commit=False)
            uf.save()
            sf = studentform.save(commit=False)
            sf.user = uf # set the user to the student form user_id
            uf.role = 1 # set the role to 1 for student in the user table
            sf.save()
            uf.save()
            
            #Login the user and redirect to the home page
            if uf is not None:
                if uf.is_active:
                    login(request, uf) # login the user
                    return redirect('accounts:home') # redirect to the home page
            
        else:
            # used dictionary to know the field and the error
            errors = {} # create a dictionary to store the errors
            # loop through the form fields and add the errors to the dictionary
            for field in userform or studentform:
                for error in field.errors:
                    errors[field.name] = error # add the error to the dictionary
            return JsonResponse({"status": False, "errors": errors})
        
    else:
        userform = UserForm()
        studentform = StudentForm()
    return render(request, 'accounts/createStudent.html', {'userform': userform, 'studentform': studentform})

# Home View 
# USed to display all the users and their details
def home(request):
    context = {
        'all_users': User.objects.all(),
    }

    return render(request, 'home.html', context)

# user_detail view
class userdetails(DetailView):
    model = User
    template_name = "accounts/user_details.html"
    
    # get context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.role == 1: # if the user is a student
            context['student'] = Student.objects.get(user_id=self.kwargs.get('pk')) # get the student details
        elif self.object.role == 2: # if the user is a teacher
            context['teacher'] = Teacher.objects.get(user_id=self.kwargs.get('pk')) # get the teacher details
        return context

