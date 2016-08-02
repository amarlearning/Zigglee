from __future__ import unicode_literals

from django.db import models

# Create your models here.
class githubBots(models.Model):
	username = models.CharField(max_length=250)
	spamflag = models.CharField(max_length=10)
