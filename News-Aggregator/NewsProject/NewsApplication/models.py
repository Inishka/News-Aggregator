from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class USER(models.Model):
    user_name=models.CharField(max_length=200, primary_key=True)
    user_mail_id=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
    
class service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_tittle=models.CharField(max_length=50)
    service_des=HTMLField()