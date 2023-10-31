from django.shortcuts import render, HttpResponse
from .models import Teacher, Student, Subject, Enrollment, Course
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.
def HelloWorld(request):
    return HttpResponse("hellow rold")

def Registration(request):
    if request.method == "POST":
        username = request.POST['usernameInput']
        password = request.POST['passwordInput']
        name = request.POST['nameInput']
        surname = request.POST['surNameInput']
        photo = request.FILES.get('photoInput')  # Get the uploaded photo

        if len(Student.objects.filter(Username=username)) > 0:
            error_message = "Username already exists"
            return render(request, 'registration.html', {'error_message': error_message})

        user = Student(Username=username, Password=password, Name=name, Surname=surname, Photo = photo)

        # if photo:  # Check if a photo was uploaded
        #     # Save the uploaded photo to the 'media' folder
        #     file_name = default_storage.save(photo.name, ContentFile(photo.read()))
        #     user.Photo = file_name

        user.save()
        
        return render(request, "registration.html", {"success_message": "User registered successfully"})
    
    

    return render(request, "registration.html")

def Login(request):
    if request.method == "POST":
        username = request.POST['usernameInput']
        password = request.POST['passwordInput']
        
        
        try:
            teacher = Teacher.objects.get(Username=username, Password=password)
            request.session['user'] = teacher
            request.session['currentRole'] = "t"
            return redirect("teacherBio")
        except:
            print("teacher login failed")

        try:
            student = Student.objects.get(Username=username, Password=password)
            
            request.session['username'] = student.Username
            request.session['currentRole'] = "s"
            return redirect("studentBio")
        except:
            print("student login failed")


        error_message = "Bad credentials"
        return render(request, 'login.html', {'error_message': error_message})

    return render(request, "login.html")

# shows student info and <ul> of links to subjects.html, teachers.html, MyCourses.html
def StudentBio(request):
    if request.session['currentRole'] == 's':
        username = request.session['username']
        student = Student.objects.get(Username = username)

        return render(request, "studentBio.html", {"user": student})
    else:
        return HttpResponse("Bad request")

# shows html page with ALL subjects list(math, pe, chemistry, english)
def Subjects(request):
    subjects = Subject.objects.all()
    return render(request, "subjects.html", {"subjects": subjects})

# shows all courses that student enrolled
def MyCourses(request):
    return None

# student cilcks on Subject and it show all Courses related to subject => cards with title and so on...
def AllCourses(request):
    return None

# details of the course, user clicks on card in AllCourses and open html page with single course
def Course(request):
    return None

# teacher info panel, see I Teach => teachCourses.html
def TeacherBio(request):
    if request.session['currentRole'] == 't':
        user = request.session['user']

        return render(request, "teacherBio.html", {"user": user})
    else:
        return HttpResponse("Bad request")

# user sees all teachers and their bio
def Teachers(request):
    return None

# single teacher, and shows courses cards he teaches => Course.html
def SingleTeacher(request):
    return None

# shows all course that teachers teaches => course.html
def TeachCourses(request):
    # join by teacher
    # coursesTeacherTeaches = Course.objects.filter(Teacher = currentTeacher)
    
    return None
