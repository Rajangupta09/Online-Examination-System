from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return 	f'{self.username}'
class Student(models.Model):
	id= models.AutoField(primary_key=True)
	category = models.CharField(max_length=200)
	sub_category = models.CharField(max_length=200)
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