from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
from django.contrib import messages
from django.db.models import Q




def login(request):
	if(request.method=="POST"):
		params=request.POST
		user=auth.authenticate(params['username'], params['password'])
		if(user is not None):
			login(request, User.objects.get(user__username=params['username']))
			messages.success(request, 'Your request has been submitted')
			return redirect('/')
		else:
			messages.error(request, 'Invalid credentials')
			return redirect('/login')
	else:
		return render(request , 'login/login.html')		


def dashboard(request):
	return render(request , 'login/dashboard.html')	


def category(request):
	categories_list = Categories.objects.all().order_by('-date_created')
	paginator = Paginator(categories_list, 10)
	page = request.GET.get('page')
	search_term=''
	paged_categorie = paginator.get_page(page)
	if(request.method=="POST"):
		post=Categories()
		post.category=request.POST.get('category')
		post.save()
		categories_list = Categories.objects.all().order_by('-date_created')
		return render(request, 'login/category.html',{'categories':paged_categorie})  
	
	if 'search' in request.GET:
		search_term = request.GET['search']
		categories_list=categories_list.filter( category__icontains=search_term)
		return render(request, 'login/category.html',{'categories':categories_list,'search_term':search_term}) 


	return render(request, 'login/category.html',{'categories':paged_categorie,'search_term':search_term}) 


def sub_category(request):
	sub_categories_list = sub_categories.objects.all().order_by('-date_created')
	categories_list = Categories.objects.all().order_by('-date_created')
	paginator = Paginator(sub_categories_list, 10)
	page = request.GET.get('page')
	search_term=''
	paged_subcategorie = paginator.get_page(page)
	if(request.method=="POST"):
		post=sub_categories()
		post.sub_category=request.POST.get('sub_category')
		post.category_id=request.POST.get('category_id')
		post.save()
		categories_list = Categories.objects.all().order_by('-date_created')
		sub_categories_list = sub_categories.objects.all().order_by('-date_created')
		return render(request, 'login/sub_category.html',{'categories':categories_list,'sub_categories':sub_categories_list,})  

	if 'search' in request.GET:
		search_term = request.GET['search']
		sub_categories_list=sub_categories_list.filter( sub_category__icontains=search_term)
		return render(request, 'login/sub_category.html',{'categories':categories_list,'sub_categories':sub_categories_list, 'search_term':search_term}) 


	return render(request, 'login/sub_category.html',{'categories':categories_list,'sub_categories':paged_subcategorie,})          

def CategoryDelete(request, pk,):
    cdelete = get_object_or_404(Categories, pk=pk)    
    if request.method=='POST':
        cdelete.delete()
        return redirect('/OnlineExam/login/category')
    return render(request, 'login/delete.html', {'cdelete': cdelete})

def SubCategoryDelete(request, pk,):
    sdelete = get_object_or_404(sub_categories, pk=pk)    
    if request.method=='POST':
        sdelete.delete()
        return redirect('/OnlineExam/login/sub_category')
    return render(request, 'login/deletesub.html', {'sdelete': sdelete})

def Categoryedit(request, pk,):
	cedit = get_object_or_404(Categories, pk=pk)    
	if request.method=='POST':
		cedit.category=request.POST.get('category')
		cedit.save()
		return redirect('/OnlineExam/login/category')
	return render(request, 'login/cedit.html',{'cedit': cedit})

def subcategoryedit(request, pk,):
	sedit = get_object_or_404(sub_categories, pk=pk)   
	categories_list = Categories.objects.all().order_by('-date_created')
	if request.method=='POST':
		sedit.sub_category=request.POST.get('sub_category')
		sedit.category_id=request.POST.get('category_id')
		sedit.save()
		return redirect('/OnlineExam/login/sub_category')
	return render(request, 'login/sedit.html', {'sedit': sedit,'categories':categories_list})


def substat(request, pk,):
	stats = get_object_or_404(sub_categories, pk=pk)   
	categories_list = Categories.objects.all().order_by('-date_created')
	if request.method=='POST':
		stats.status=request.POST.get('status')
		stats.save()
		return redirect('/OnlineExam/login/sub_category')
	return render(request, 'login/stats.html', {'stats': stats,'categories':categories_list})

def cstat(request, pk,):
	statc = get_object_or_404(Categories, pk=pk)    
	if request.method=='POST':
		statc.status=request.POST.get('status')
		statc.save()
		return redirect('/OnlineExam/login/category')
	return render(request, 'login/statc.html',{'statc': statc})

def Subject(request):
	subject_list = Subjects.objects.all().order_by('-date_created')
	categors = Subjects.objects.get(sub_categories__category = self.object.category)
	sub_categories_list = sub_categories.objects.all().order_by('-date_created')
	paginator = Paginator(subject_list, 10)
	page = request.GET.get('page')
	search_term=''
	paged_subject = paginator.get_page(page)
	if(request.method=="POST"):
		post=Subjects()
		post.sub_category_id=request.POST.get('sub_category')
		post.subject=request.POST.get('subject')
		post.save()
		subject_list = Subjects.objects.all().order_by('-date_created')
		sub_categories_list = sub_categories.objects.all().order_by('-date_created')
		return render(request, 'login/subject.html',{'sub_categories':sub_categories_list,'Subject':subject_list})  

	if 'search' in request.GET:
		search_term = request.GET['search']
		subject_list=subject_list.filter( subject__icontains=search_term)
		return render(request, 'login/subject.html',{'subject':subject_list, 'search_term':search_term})
	return render(request, 'login/subject.html',{'sub_categories':sub_categories_list,'Subject':paged_subject,})          
