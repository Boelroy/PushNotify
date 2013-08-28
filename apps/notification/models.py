from django.db import models

# Create your models here.
class Users(models.Model):
	"""docstring for Users"""
	name = models.CharField(max_length=30)
	lastonLineTime = models.DateTimeField()
	onlineStatus = models.BooleanField()
	ip = models.IPAddressField()
	