from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver
from Home.models import Industry
#from Accounts.models import User

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='employer_user')
    company_name = models.CharField(max_length=50)
    company_description = models.TextField()
    phone_number = models.CharField(max_length=50)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='industry')
    logo = models.ImageField(upload_to='company_logos')