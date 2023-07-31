from django.contrib.auth.models import AbstractUser
from django.db import models


class Operator(AbstractUser):
	caa_code = models.CharField(verbose_name='CAA Code', max_length=40, unique=True, null=True)
	file1 = models.FileField(verbose_name='Certificat A1/A3', null=True, blank=True, upload_to='static/certificates/')
	file2 = models.FileField(verbose_name='Certificat A2', null=True, blank=True, upload_to='static/certificates/')
	# email = models.EmailField(verbose_name='Email address', max_length=255, unique=True)
	# USERNAME_FIELD = 'email'

	def __str__(self):
		return self.caa_code


class Aircraft(models.Model):
	name = models.CharField(max_length=40)
	owner = models.ForeignKey(Operator, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Certificates(models.Model):
	document = models.FileField(upload_to='static/certificates')
	user = models.ForeignKey(Operator, on_delete=models.CASCADE)


class FlightLog(models.Model):
	operator = models.ForeignKey(Operator, on_delete=models.CASCADE)  # CAA.ro code
	aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)  # aircraft name
	longitude = models.FloatField(null=True, blank=True)  # location
	latitude = models.FloatField(null=True, blank=True)  # location
	details = models.TextField(null=True, blank=True)  # mission - photo, video, recon, job
	batteries_flown = models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.operator}: Lat:{self.latitude}, Long:{self.longitude}, at {self.created_at}'


class Contact(models.Model):
	last_name = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	question = models.TextField(max_length=300)
	email = models.EmailField(max_length=50)

	def __str__(self):
		return f'{self.first_name} {self.last_name} has a question'
