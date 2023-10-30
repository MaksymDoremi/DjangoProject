from django.contrib import admin
from .models import Student, Teacher, Course, Subject, Enrollment

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Enrollment)