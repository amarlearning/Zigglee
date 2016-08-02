from __future__ import unicode_literals
from django.db import models

# Create your models here.
class githubBots(models.Model):
	username = models.CharField(max_length=250)
	spamflag = models.CharField(max_length=10)

	def __str__(self):
		return self.username


class repository(models.Model):
	name = models.CharField(max_length=1000)
	stars = models.CharField(max_length=5)
	datetime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name