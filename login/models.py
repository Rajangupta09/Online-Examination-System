from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class login(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	def __str__(self):
		return 	f'{self.username}'


class Profile(models.Model):
	user = models.OneToOneField(User ,on_delete=models.CASCADE)	
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):
		return f'{self.user}'


class Categories(models.Model):
	id = models.AutoField(primary_key=True)
	category = models.CharField(max_length=100)
	date_created = models.DateTimeField(default=timezone.now)
	status = models.BooleanField(default=True)
	def __str__(self):
		return f'{self.category}'

class sub_categories(models.Model):
	id=models.AutoField(primary_key=True)
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categories')
	date_created = models.DateTimeField(default=timezone.now)
	status = models.BooleanField(default=True)
	sub_category = models.CharField(max_length=200)
	def __str__(self):
	 return self.sub_category

class Subjects(models.Model):
	id=models.AutoField(primary_key=True)
	sub_category = models.ForeignKey(sub_categories, on_delete=models.CASCADE, related_name='subject_sub_categories')
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='subject_categories')
	date_created = models.DateTimeField(default=timezone.now)
	subject = models.CharField(max_length=200)
	status = models.BooleanField(default=True)
	def __str__(self):
	 return f'{self.subject}'


class Center(models.Model):
	center_code=models.IntegerField(primary_key=True)
	Name = models.CharField(max_length=200)
	Address = models.TextField()
	Email = models.EmailField(max_length=200)
	Username = models.CharField(max_length=200)
	Password = models.CharField(max_length=200)
	status = models.BooleanField(default=True)
	def __str__(self):
		return self.Name
class Student(models.Model):
	id= models.AutoField(primary_key=True)
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='student_category')
	center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='student_center')
	Name = models.CharField(max_length=200)
	father_name= models.CharField(max_length=200)
	mother_name = models.CharField(max_length=200)
	DOB = models.DateField()
	Address = models.TextField()
	Phone = models.BigIntegerField()
	Email = models.EmailField()
	status = models.BooleanField(default=True)
	Password = models.CharField(max_length=200)
	def __str__(self):
	 return self.Name

class Exam(models.Model):
	id=models.AutoField(primary_key=True)
	sub_category = models.ForeignKey(sub_categories, on_delete=models.CASCADE, related_name='exam_subcategories')
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='exam_categories')
	subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='exam_subject')
	Name = models.CharField(max_length=200)
	exam_date = models.DateField()
	exam_duration = models.DurationField(default='00:00:00')
	pass_percentage = models.IntegerField()
	reexam_date = models.DateField()
	negative_marking = models.BooleanField(default=False, blank=True, null=True )
	tandc = models.TextField()
	status = models.BooleanField(default=True)
	resultonmail = models.BooleanField(default=False, blank=True, null=True)

	def __str__(self):
	 return self.Name

class Question(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE)
	marks = models.PositiveIntegerField(default=0)
	question = models.TextField(max_length=500)
	status = models.BooleanField(default=True)
	option1 = models.CharField(max_length=100, null=True)
	option2 = models.CharField(max_length=100, null=True)
	option3 = models.CharField(max_length=100, null=True)
	option4 = models.CharField(max_length=100, null=True)
	choose = (('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4'))
	answer = models.CharField(max_length=1, choices=choose)
	def __str__(self):
		return str(self.question)