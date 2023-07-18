from django.db import models

# Create your models here.


class Flight(models.Model):
	operator_id = models.CharField(max_length=40)  # CAA.ro code
	aircraft = models.CharField(max_length=40) #aircraft name
	operator_name = models.CharField(max_length=40) #CAA.ro code
	longitude = models.IntegerField(max_length=20) #location
	latitude = models.IntegerField(max_length=20) # location
	details = models.TextField(max_length=200) #mission - photo, video, recon, job
	batteries_flown = models.IntegerField(max_length=2) #1-99
	date = models.DateTimeField
