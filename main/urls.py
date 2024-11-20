from django.urls import path, include
from . import views
# main/urls.py
# from main import views, user_login



urlpatterns = [
    path('', views.home, name='home'),
    path('base', views.base, name='base'), 
    path('singleCourse', views.single_course, name='single_course'),
    path('contact', views.contact_us, name='contact_us'),
    path('about', views.about_us, name='about_us'),
    
    path('accounts/register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('profile/', views.profile, name='profile'),
    path('enrolled-courses/', views.enrolled_courses, name='enrolled_courses'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
]
