from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html') ,name='logout'),
    path('login/dashboard/', views.dashboard ,name='home'),
    path('login/category/', views.category ,name='category'), 
    path('login/sub_category/', views.sub_category ,name='sub_category'),
    path('login/Subject/', views.Subject ,name='subject'),  
    path('login/Center/', views.center, name='center'),
    path('login/Student/', views.student, name='student'),
    path('login/Exam/', views.exam ,name='exam'),  
    path('login/Question/', views.question ,name='question'),  


    path('delete_Exam/<int:pk>', views.examDelete , name='exam_delete'),
    path('delete_Center/<int:pk>', views.centerDelete , name='center_delete'),
    path('delete_Student/<int:pk>', views.studentDelete , name='student_delete'),
    path('delete/<int:pk>', views.CategoryDelete , name='Category_delete'),
    path('delete_SubCategory/<int:pk>', views.SubCategoryDelete , name='Sub_Category_delete'),
    path('delete_Subject/<int:pk>', views.SubjectDelete , name='subject_delete'),



    path('Edit/<int:pk>/', views.Categoryedit , name='category_edit'),
    path('Edit_Subcategory/<int:pk>/', views.subcategoryedit , name='subcategory_edit'),
    path('Edit_Subject/<int:pk>/', views.SubjectEdit , name='subject_edit'),
    path('Edit_Center/<int:pk>/', views.CenEdit , name='center_edit'),
    path('Edit/<int:pk>/', views.studentEdit , name='student_edit'),
    path('Edit_Center/<int:pk>/', views.CenEdit , name='center_edit'),
    path('Edit_Exam/<int:pk>/', views.examedit , name='exam_edit'),



    path('Status_Student/<int:pk>/', views.studentstat , name='statc'),
    path('Status_Subcategory/<int:pk>/', views.substat , name='substat'),
    path('Status_category/<int:pk>/', views.cstat , name='statc'),
    path('Status_subject/<int:pk>/', views.subjectstat , name='subjstat'),
    path('Status_Center/<int:pk>', views.centerstat , name='centerstat'),
    path('Status_Exam/<int:pk>/', views.examstat , name='examstat'),



    path('load-subject/', views.load_sub, name='loadsub'),
    path('load-exam/', views.load_exam, name='loadexam'),




]    

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)