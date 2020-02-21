from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
from django.contrib import messages, auth
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



#Category
def category(request):
	categories_list = Categories.objects.all().order_by('-date_created')
	total = Categories.objects.count()
	dis=int(total/3)
	paginator = Paginator(categories_list, dis)
	page = request.GET.get('page')
	search_term=''
	paged_categorie = paginator.get_page(page)
	if(request.method=="POST"):
		post=Categories()
		post.category=request.POST.get('category')
		post.save()
		categories_list = Categories.objects.all().order_by('-date_created')
		messages.success(request, 'Your request has been submitted')
		return render(request, 'login/category.html',{'categories':paged_categorie})  
	
	if 'search' in request.GET:
		search_term = request.GET['search']
		categories_list=categories_list.filter( category__icontains=search_term)
		return render(request, 'login/category.html',{'categories':categories_list,'search_term':search_term}) 


	if 'view' in request.GET:
		dis = request.GET['view']
		paginator = Paginator(categories_list, dis)
		page = request.GET.get('page')
		paged_categorie = paginator.get_page(page)
		return render(request, 'login/category.html',{'categories':paged_categorie, 'list':dis,'total':total}) 
	return render(request, 'login/category.html',{'categories':paged_categorie, 'list':dis,'total':total}) 


def CategoryDelete(request, pk,):
	cdelete = get_object_or_404(Categories, pk=pk)    
	if request.method=='POST':
		cdelete.delete()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/category')
	return render(request, 'login/delete.html', {'cdelete': cdelete})


def Categoryedit(request, pk,):
	cedit = get_object_or_404(Categories, pk=pk)    
	if request.method=='POST':
		cedit.category=request.POST.get('category')
		cedit.save()
		messages.success(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/category')
	return render(request, 'login/cedit.html',{'cedit': cedit})

def cstat(request, pk,):
	statc = get_object_or_404(Categories, pk=pk)    
	if request.method=='POST':
		statc.status=request.POST.get('status')
		statc.save()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/category')
	return render(request, 'login/statc.html',{'statc': statc})

#SUB CATEGORY
def sub_category(request):
	sub_categories_list = sub_categories.objects.all().order_by('-date_created')
	total = sub_categories.objects.count()
	categories_list = Categories.objects.all().order_by('-date_created')
	dis=10
	paginator = Paginator(sub_categories_list, dis)
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
		messages.success(request, 'Your request has been submitted')
		return render(request, 'login/sub_category.html',{'categories':categories_list,'sub_categories':paged_subcategorie,})  

	if 'search' in request.GET:
		search_term = request.GET['search']
		sub_categories_list=sub_categories_list.filter( sub_category__icontains=search_term)
		return render(request, 'login/sub_category.html',{'categories':categories_list,'sub_categories':sub_categories_list, 'search_term':search_term}) 

	if 'view' in request.GET:
		dis = request.GET['view']
		paginator = Paginator(sub_categories_list, dis)
		page = request.GET.get('page')
		paged_subcategorie = paginator.get_page(page)
		return render(request, 'login/sub_category.html',{'categories':categories_list,'sub_categories':paged_subcategorie, 'list':dis,'total':total})          

	return render(request, 'login/sub_category.html',{'categories':categories_list,'sub_categories':paged_subcategorie, 'list':dis,'total':total})          


def subcategoryedit(request, pk,):
	sedit = get_object_or_404(sub_categories, pk=pk)   
	categories_list = Categories.objects.all().order_by('-date_created')
	if request.method=='POST':
		sedit.sub_category=request.POST.get('sub_category')
		sedit.category_id=request.POST.get('category_id')
		sedit.save()
		messages.success(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/sub_category')
	return render(request, 'login/sedit.html', {'sedit': sedit,'categories':categories_list})

def SubCategoryDelete(request, pk,):
	sdelete = get_object_or_404(sub_categories, pk=pk)    
	if request.method=='POST':
		sdelete.delete()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/sub_category')
	return render(request, 'login/delete.html', {'sdelete': sdelete})

def substat(request, pk,):
	statc = get_object_or_404(sub_categories, pk=pk)   
	categories_list = Categories.objects.all().order_by('-date_created')
	if request.method=='POST':
		statc.status=request.POST.get('status')
		statc.save()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/sub_category')
	return render(request, 'login/statc.html', {'statc': statc,'categories':categories_list})

#SUBJECT
def Subject(request):
	subject_list = Subjects.objects.all().order_by('-date_created')
	total = Subjects.objects.count()
	categories_list = Categories.objects.all().order_by('-date_created')
	sub_categories_list = sub_categories.objects.all().order_by('-date_created')
	dis=10
	paginator = Paginator(subject_list, dis)
	page = request.GET.get('page')
	search_term=''
	paged_subject = paginator.get_page(page)
	if(request.method=="POST"):
		post=Subjects()
		post.category_id=request.POST.get('category')
		post.sub_category_id=request.POST.get('sub_category')
		post.subject=request.POST.get('subject')
		messages.success(request, 'Your request has been submitted')
		post.save()
		subject_list = Subjects.objects.all().order_by('-date_created')
		sub_categories_list = sub_categories.objects.all().order_by('-date_created')
		return render(request, 'login/subject.html',{'sub_categories':sub_categories_list,'Subject':subject_list, 'categories':categories_list})  

	if 'search' in request.GET:
		search_term = request.GET['search']
		subject_list=subject_list.filter( subject__icontains=search_term)
		return render(request, 'login/subject.html',{'Subject':subject_list, 'search_term':search_term})
	if 'view' in request.GET:
		dis = request.GET['view']
		paginator = Paginator(subject_list, dis)
		page = request.GET.get('page')
		paged_subject = paginator.get_page(page)
		return render(request, 'login/subject.html',{'sub_categories':sub_categories_list,'Subject':paged_subject,'categories':categories_list,'list':dis,'total':total})          
		
	return render(request, 'login/subject.html',{'sub_categories':sub_categories_list,'Subject':paged_subject,'categories':categories_list,'list':dis,'total':total})          

def SubjectDelete(request, pk,):
	subdelete = get_object_or_404(Subjects, pk=pk)    
	if request.method=='POST':
		subdelete.delete()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Subject/')
	return render(request, 'login/delete.html', {'subdelete': subdelete})

def SubjectEdit(request, pk,):
	Subedit = get_object_or_404(Subjects, pk=pk)   
	categories_list = Categories.objects.all().order_by('-date_created')
	sub_categories_list = sub_categories.objects.all().order_by('-date_created')
	if request.method=='POST':
		Subedit.sub_category_id=request.POST.get('sub_category')
		Subedit.subject=request.POST.get('subject')
		Subedit.save()
		messages.success(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Subject')
	return render(request, 'login/subedit.html', {'Subedit': Subedit,'categories':categories_list,'sub_categories':sub_categories_list})


def subjectstat(request, pk,):
	statc = get_object_or_404(Subjects, pk=pk)   
	if request.method=='POST':
		statc.status=request.POST.get('status')
		statc.save()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Subject/')
	return render(request, 'login/statc.html', {'statc': statc})

def load_sub(request):
    category_id = request.GET.get('category')
    sub_category = sub_categories.objects.filter(category_id=category_id).order_by('date_created')
    return render(request, 'login/option.html', {'sub_category': sub_category})


#Center
def center(request):
	center=Center.objects.all().order_by('center_code')
	total=Center.objects.count()
	search_term=''
	dis=10
	paginator = Paginator(center, dis)
	page = request.GET.get('page')
	search_term=''
	paged_center = paginator.get_page(page)
	if request.method=='POST':
		post=Center()
		post.center_code=request.POST.get('code')
		post.Name=request.POST.get('name')
		post.Address=request.POST.get('address')
		post.Email=request.POST.get('email')
		post.Username=request.POST.get('user')
		post.Password=request.POST.get('password')
		messages.success(request, 'Your request has been submitted')
		post.save()
		return redirect('/OnlineExam/login/Center/')
	if 'search' in request.GET:
		search_term = request.GET['search']
		center=center.filter( Name__icontains=search_term)
		return render(request, 'login/center.html',{'center': center,'search_term':search_term,}) 
	if 'view' in request.GET:
		dis = request.GET['view']
		paginator = Paginator(center, dis)
		page = request.GET.get('page')
		paged_center = paginator.get_page(page)
		return render(request, 'login/center.html', {'center':paged_center,'list':dis,'total':total})
	return render(request, 'login/center.html', {'center':paged_center,'list':dis,'total':total})

def centerstat(request, pk,):
	statc = get_object_or_404(Center, pk=pk)   
	if request.method=='POST':
		statc.status=request.POST.get('status')
		statc.save()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Center/')
	return render(request, 'login/statc.html', {'statc': statc})

def centerDelete(request, pk,):
	cendelete = get_object_or_404(Center, pk=pk)    
	if request.method=='POST':
		cendelete.delete()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Center/')
	return render(request, 'login/delete.html', {'cendelete': cendelete})

def CenEdit(request, pk,):
	cenedit = get_object_or_404(Center, pk=pk)   
	if request.method=='POST':
		cenedit.Name=request.POST.get('name')
		cenedit.Address=request.POST.get('address')
		cenedit.Email=request.POST.get('email')
		cenedit.Username=request.POST.get('user')
		cenedit.Password=request.POST.get('password')
		cenedit.save()
		messages.success(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Center/')
	return render(request, 'login/cenedit.html', {'cenedit': cenedit})

def student(request):
	student = Student.objects.all().order_by('id')
	total = Student.objects.count()
	center=Center.objects.all().order_by('center_code')
	categories_list = Categories.objects.all().order_by('-date_created')
	search_term=''
	dis=10
	total = Student.objects.count()
	paginator = Paginator(student, dis)
	page = request.GET.get('page')
	search_term=''
	paged_student = paginator.get_page(page)
	if request.method=='POST':
		post=Student()
		post.category_id=request.POST.get('category')
		post.center_id=request.POST.get('center')
		post.Name=request.POST.get('name')
		post.father_name=request.POST.get('fname')
		post.mother_name=request.POST.get('mname')
		post.DOB = request.POST.get('date')
		post.Phone = request.POST.get('phone')
		post.Address = request.POST.get('address')
		post.Email=request.POST.get('email')
		post.Password=request.POST.get('password')
		post.save()
		messages.success(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Student/')

	if 'search' in request.GET:
		search_term = request.GET['search']
		student=student.filter(Name__icontains=search_term)
		return render(request, 'login/student.html',{'student':student,'search_term':search_term}) 

	if 'view' in request.GET:
		dis = request.GET['view']
		paginator = Paginator(student, dis)
		page = request.GET.get('page')
		paged_student = paginator.get_page(page)
		return render(request, 'login/student.html',{'student':paged_student, 'center':center, 'categories': categories_list, 'list':dis,'total':total}) 
	return render(request, 'login/student.html', {'student':paged_student, 'center':center, 'categories': categories_list, 'list':dis,'total':total})

def studentstat(request, pk,):
	statc = get_object_or_404(Student, pk=pk)   
	if request.method=='POST':
		statc.status=request.POST.get('status')
		statc.save()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Student/')
	return render(request, 'login/statc.html', {'statc': statc})

def studentDelete(request, pk,):
	studelete = get_object_or_404(Student, pk=pk)    
	if request.method=='POST':
		studelete.delete()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Student/')
	return render(request, 'login/delete.html', {'studelete': studelete})

def studentEdit(request, pk,):
	stuedit = get_object_or_404(Student, pk=pk)   
	if request.method=='POST':
		stuedit.category_id=request.POST.get('category')
		stuedit.center_id=request.POST.get('center')
		stuedit.Name=request.POST.get('name')
		stuedit.father_name=request.POST.get('fname')
		stuedit.mother_name=request.POST.get('mname')
		stuedit.DOB = request.POST.get('date')
		stuedit.Phone = request.POST.get('phone')
		stuedit.Address = request.POST.get('address')
		stuedit.Email=request.POST.get('email')
		stuedit.Password=request.POST.get('password')
		stuedit.save()
		messages.success(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Student/')
	return render(request, 'login/stuedit.html', {'stuedit': stuedit})

def exam(request):
	subject_list = Subjects.objects.all().order_by('-date_created')
	categories_list = Categories.objects.all().order_by('-date_created')
	sub_categories_list = sub_categories.objects.all().order_by('-date_created')
	exam_list = Exam.objects.all()
	dis=10
	total = Exam.objects.count()
	paginator = Paginator(exam_list, dis)
	page = request.GET.get('page')
	search_term=''
	paged_exam = paginator.get_page(page)
	if(request.method=="POST"):
		post=Exam()
		post.category_id=request.POST.get('category')
		post.sub_category_id=request.POST.get('sub_category')
		post.subject_id=request.POST.get('subject')
		post.Name=request.POST.get('name')
		post.exam_date=request.POST.get('date')
		post.exam_duration=request.POST.get('duration')
		post.pass_percentage=request.POST.get('pp')
		post.reexam_date=request.POST.get('redate')
		post.negative_marking=request.POST.get('nm')
		post.tandc=request.POST.get('tc')
		post.resultonmail=request.POST.get('rm')
		messages.success(request, 'Your request has been submitted')
		post.save()
		  
	if 'search' in request.GET:
		search_term = request.GET['search']
		exam_list=exam_list.filter(Name__icontains=search_term)
		return render(request, 'login/exam.html',{'exam':exam_list, 'search_term':search_term})
	if 'view' in request.GET:
		dis = request.GET['view']
		paginator = Paginator(exam_list, dis)
		page = request.GET.get('page')
		paged_exam = paginator.get_page(page)
		return render(request, 'login/exam.html',{'sub_categories':sub_categories_list,'exam':paged_exam,'categories':categories_list,'list':dis,'total':total})          
	return render(request, 'login/exam.html',{'sub_categories':sub_categories_list,'exam':paged_exam,'categories':categories_list,'list':dis,'total':total})          

def load_exam(request):
	category_id = request.GET.get('category')
	sub_category_id = request.GET.get('sub')
	subject = Subjects.objects.filter(Q(category_id=category_id) | Q(sub_category_id=sub_category_id)).order_by('date_created')
	return render(request, 'login/option1.html', {'subject': subject})

	
def examstat(request, pk,):
	statc = get_object_or_404(Exam, pk=pk)   
	if request.method=='POST':
		statc.status=request.POST.get('status')
		statc.save()
		messages.info(request, 'Your request has been submitted')		
		return redirect('OnlineExam/login/Exam/')
	return render(request, 'login/statc.html', {'statc': statc})

def examDelete(request, pk,):
	examdelete = get_object_or_404(Exam, pk=pk)    
	if request.method=='POST':
		examdelete.delete()
		messages.info(request, 'Your request has been submitted')
		return redirect('OnlineExam/login/Exam/')
	return render(request, 'login/delete.html', {'examdelete': examdelete})

def examedit(request, pk,):
	examedit = get_object_or_404(Exam, pk=pk)   
	if request.method=='POST':
		examedit.Name=request.POST.get('name')
		examedit.exam_date=request.POST.get('date')
		examedit.exam_duration=request.POST.get('duration')
		examedit.pass_percentage=request.POST.get('pp')
		examedit.reexam_date=request.POST.get('redate')
		examedit.negative_marking=request.POST.get('nm')
		examedit.tandc=request.POST.get('tc')
		examedit.resultonmail=request.POST.get('rm')
		examedit.save()
		messages.success(request, 'Your request has been submitted')
		return redirect('OnlineExam/login/Exam/') 
	return render(request, 'login/examedit.html', {'examedit': examedit})

def question(request):
	ques= Question.objects.all()
	total= Question.objects.count()
	exam_list = Exam.objects.all()
	dis=10
	paginator = Paginator(ques, dis)
	page = request.GET.get('page')
	search_term=''
	paged_ques = paginator.get_page(page)
	if(request.method=="POST"):
		post=Question()
		post.question=request.POST.get('editor1')
		post.marks=request.POST.get('marks')
		post.exam_name_id=request.POST.get('exam')
		post.option1=request.POST.get('option1')
		post.option2=request.POST.get('option2')
		post.option3=request.POST.get('option3')
		post.option4=request.POST.get('option4')
		post.answer=request.POST.get('answer')
		post.save()
		messages.success(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Question/')

	if 'search' in request.GET:
		search_term = request.GET['search']
		ques=ques.filter(question__icontains=search_term)
		return render(request, 'login/question.html',{'exam':exam_list, 'Question': ques, 'search_term':search_term})
	if 'view' in request.GET:
		dis = request.GET['view']
		paginator = Paginator(ques, dis)
		page = request.GET.get('page')
		paged_ques = paginator.get_page(page)
		return render(request, 'login/question.html', {'Question': paged_ques, 'exam':exam_list,'list':dis,'total':total })
	return render(request, 'login/question.html', {'Question': paged_ques, 'exam':exam_list,'list':dis,'total':total })

	
def quesstat(request, pk,):
	statc = get_object_or_404(Question, pk=pk)   
	if request.method=='POST':
		statc.status=request.POST.get('status')
		statc.save()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Question/')
	return render(request, 'login/statc.html', {'statc': statc})

def quesDelete(request, pk,):
	quesdelete = get_object_or_404(Question, pk=pk)    
	if request.method=='POST':
		quesdelete.delete()
		messages.info(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Exam/')
	return render(request, 'login/delete.html', {'examdelete': quesdelete})

def quesedit(request, pk,):
	quesedit = get_object_or_404(Question, pk=pk) 
	exam_list = Exam.objects.all()
	if request.method=='POST':
		quesedit.question=request.POST.get('editor1')
		quesedit.marks=request.POST.get('marks')
		quesedit.exam_name_id=request.POST.get('exam')
		quesedit.option1=request.POST.get('option1')
		quesedit.option2=request.POST.get('option2')
		quesedit.option3=request.POST.get('option3')
		quesedit.option4=request.POST.get('option4')
		quesedit.answer=request.POST.get('answer')
		quesedit.save()
		messages.success(request, 'Your request has been submitted')
		return redirect('/OnlineExam/login/Question/') 
	return render(request, 'login/quesedit.html', {'quesedit': quesedit,'exam':exam_list})
