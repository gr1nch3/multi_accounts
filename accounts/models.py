from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Role selection for the user 
User_Role = ((1, 'Student'), (2, 'Teacher'))

# User Model
# You can add more fields to the user model if you want.
class User(AbstractUser):
    email      = models.EmailField(max_length=50, unique=True, )
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # The role field will make it possible to 
    # call out data realting to the user's role(ie: teacher or student).
    role       = models.IntegerField(choices=User_Role, default=0)
    username = None # 
    
    USERNAME_FIELD = "email" # used email to authenticate the user
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.first_name

# Subject class for teachers 
class Subjects(models.Model):
    name      = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# Other models
# Teacher model
class Teacher(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    #add extra details here
    grades    = models.IntegerField()
    subjects  = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name

# Student model
class Student(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    #add extra details here
    grade     = models.IntegerField()
    age       = models.IntegerField()
    
    def __str__(self):
        return self.user.first_name
