from django.db import models

# Create your models here.
class Profile(models.Model):
	num = models.CharField(max_length=10,blank=False)
	detail = models.TextField(blank=False)

	def __str__(self):
		return self.num



class Service(models.Model):
	name = models.CharField(max_length=50,blank=False)
	detail = models.TextField(blank=False)

	def __str__(self):
		return self.name



class Training(models.Model):
	year = models.CharField(max_length=30,blank=False)
	institute = models.CharField(max_length=200,blank=False)
	detail = models.TextField(blank=False)
	img = models.ImageField(blank=False)

	def __str__(self):
		return self.year


class DevServe(models.Model):
	name = models.CharField(blank=False,max_length=200)
	detail = models.TextField(blank=False)

	def __str__(self):
		return self.name



class Consult(models.Model):
	heading = models.CharField(max_length=200,blank=False)
	detail = models.TextField(blank=False)
	img = models.ImageField(blank=False)

	def __str__(self):
		return "Consult Detail"



class Contact(models.Model):
	name = models.CharField(max_length=200,blank=False)
	email = models.EmailField(blank=False)
	phone = models.CharField(blank=False,max_length=20)
	city = models.CharField(blank=False,max_length=50)
	msg = models.TextField(blank=False)

	def __str__(self):
		return self.name


class Link(models.Model):
	name = models.CharField(max_length=200,blank=False)
	detail = models.TextField(blank=False)

	def __str__(self):
		return self.name


class ProfileImg(models.Model):
	name = models.CharField(max_length=20,blank=False)
	img = models.ImageField(blank=False)

	def __str__(self):
		return self.name