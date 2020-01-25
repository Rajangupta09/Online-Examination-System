from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html') ,name='logout'),
    path('login/dashboard/', views.dashboard ,name='home'),
    path('login/category/', views.category ,name='category'),
]    

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)