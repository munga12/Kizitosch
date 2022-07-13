from . import views
from django.urls import path

# the foward slash should always come after the url name
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.signIn, name='signIn'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/createCourse/", views.createCourse, name="createCourse"),
    #path("signup/", views.signup, name="signup"),
    #path("login/", views.login, name="login"),
    path("", views.home, name="home")
]