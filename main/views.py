from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from main.models import Category, Course




def base(request):
    return render(request, 'base.html')

def home(request):
    categories = Category.objects.all().order_by('id')[0:5]
    courses = Course.objects.filter(status= 'PUBLISH').order_by('-id')
    
    
    context= {
        'categories' : categories,
        'courses' : courses,
        
    }
    return render(request, 'main/home.html', context)

def single_course(request):
    return render(request, 'main/single_course.html')

def contact_us(request):
    return render(request, 'main/contact_us.html')

def about_us(request):
    return render(request, 'main/about_us.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # check enmial
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists!')
            return redirect('register')
        
        # check username
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'User Name already exists!')
            return redirect('register')
        user= User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')
    
        
    return render(request, 'registration/register.html')

def profile(request):
    return render(request, 'profile.html')  # Your profile page

@login_required
def enrolled_courses(request):
    return render(request, 'enrolled_courses.html')  # List of enrolled courses

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logging out

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # If already logged in, redirect to home

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            # Authenticate user with username and password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
        except User.DoesNotExist:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})

    return render(request, 'registration/login.html')



def update_profile(request):
    return render(request,'registration/update_profile.html')

def updated_profile(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firs_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id
        
        user = User.objects.get(id=user_id)
        user.first_name = firs_name
        user.last_name = last_name
        user.username = username
        user.email = email
        
        if password != None and password != "":
            user.set_password(password)
        
        user.save()
        messages.success(request, "Profile Successfully Updated.")
        return redirect('update_profile')