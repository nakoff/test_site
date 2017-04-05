from django.db import models

class User(models.Model):
	user = models.CharField(max_length=50)
	def publish(self):
		self.save()

	def __str__(self):
		return self.user

class Category(models.Model):
	user  = models.ForeignKey(User)
	cat = models.CharField(max_length=200)
	def __str__(self):
		return self.cat

class Contest(models.Model):
	cat  = models.ForeignKey(Category)
	name = models.CharField(max_length=200)
	date = models.CharField(max_length=200)
	result = models.CharField(max_length=20)
	def __str__(self):
		return self.name

