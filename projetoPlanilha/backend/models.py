from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField(20)
    password = models.CharField(20)
    
    
    