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
    path('delete/<int:pk>', views.CategoryDelete , name='Category_delete'),
    path('delete_SubCategory/<int:pk>', views.SubCategoryDelete , name='Sub_Category_delete'),
    path('delete_Subject/<int:pk>', views.SubjectDelete , name='subject_delete'),
    path('Edit/<int:pk>', views.Categoryedit , name='category_edit'),
    path('Edit_Subcategory/<int:pk>', views.subcategoryedit , name='subcategory_edit'),
    path('Edit_Subject/<int:pk>', views.SubjectEdit , name='subject_edit'),
    path('Status_Subcategory/<int:pk>', views.substat , name='substat'),
    path('Status_category/<int:pk>', views.cstat , name='statc'),
    path('Status_subject/<int:pk>', views.subjectstat , name='subjstat'),
    path('load-subject', views.load_sub, name='loadsub'),

]    

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)