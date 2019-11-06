from django.db import models

# Create your models here.
class Userdetail(models.Model):
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	email = models.EmailField()
	contact = models.IntegerField()
	password = models.CharField(max_length=128, default='GKt15sdgn@6')
	cpassword = models.CharField(max_length=128, default='GKt15sdgn@6')
	def __str__(self):
		return self.fname
