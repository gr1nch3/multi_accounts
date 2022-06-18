from django.contrib import admin
from accounts.models import User, Teacher, Student, Subjects

# Register your models here.
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subjects)