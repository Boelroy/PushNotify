from django.db import models

# Create your models here.
class Users(models.Model):
	"""the Model of the Notification Users"""
	name = models.CharField(max_length=30)
	lastonLineTime = models.DateTimeField()
	onlineStatus = models.BooleanField()
	ip = models.IPAddressField()



class OffLineNotification(models.Model):
	""" Model of Notification that no 
		pushed to the user
	"""
	note = models.CharField(max_length=7000)
	notifiUsername = models.CharField(max_length=30)

	