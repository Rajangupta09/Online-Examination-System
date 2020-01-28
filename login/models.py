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
	 return f'{self.sub_category}'