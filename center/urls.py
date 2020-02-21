from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='center/login.html'),name='login'),
    path('Student/',views.addstudent,name='student')
]