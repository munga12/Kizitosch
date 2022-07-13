from django.shortcuts import redirect, render
from kizito_sch.models import Courses, Users
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home/index.html')
'''
def login(request):
    return render(request, 'auth/login.html')

def signup(request):
    return render(request, 'auth/signup.html')
 '''   

def dashboard(request):
    return render(request, 'dashboard/index.html')

# def a register function that creates users and save them to the database
def signIn(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(usename=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/dashboard')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'auth/login.html',context={'form':AuthenticationForm()})

def register(request):
    if request.method == 'POST':
        # get the form data
        usename = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # create a new user
        user = Users(usename=usename, email=email, password=password)
        # save the user to the database
        user.save()
        # redirect to the login page
        return redirect('/login')
    else:
        return render(request, 'auth/signup.html')

#add corses to the database
def createCourse(request):
    if request.method == 'POST':
        # get the form data
        course_name = request.POST['course_name']
        course_image = request.POST['course_image']
        course_description = request.POST['course_description']
        # create a new course
        course = Courses(course_name=course_name, course_image=course_image, course_description=course_description)
        # save the course to the database
        course.save()
        
    else:
        return render(request, 'dashboard/index.html')