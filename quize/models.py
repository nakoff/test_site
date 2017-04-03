from django.db import models

from django.utils import timezone

class Post(models.Model):
	user = models.CharField(max_length=50)
	def publish(self):
		self.save()

	def __str__(self):
		return self.user

class Vid(models.Model):
	post  = models.ForeignKey(Post)
	vid = models.CharField(max_length=100)
	def __str__(self):
		return self.vid

class Kon(models.Model):
	vid  = models.ForeignKey(Vid)
	name = models.CharField(max_length=200)
	date = models.CharField(max_length=200)
	result = models.CharField(max_length=20)
	def __str__(self):
		return self.name
