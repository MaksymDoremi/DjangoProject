from django.urls import path
from . import views

urlpatterns = [
    path("", views.HelloWorld, name="home"), 
    path("registration/", views.Registration, name="registration"), 
    path("login/", views.Login, name="login"), 
    path("studentBio/", views.StudentBio, name="studentBio"), 
    path("teacherBio/", views.TeacherBio, name="teacherBio"), 
    path("subjects/", views.Subjects, name="subjects"),
    path("teachers/", views.Teachers, name="teachers"),
    path("teacher/", views.SingleTeacher, name="teacher"),  
    path("myCourses/", views.MyCourses, name="myCourses"),
    path("allCourses/<int:subject_id>", views.AllCourses, name="allCourses"),
    path("course/", views.SingleCourse, name="course"),
    path("teachCourses/", views.TeachCourses, name="teachCourses")
]