from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    verify_password = models.CharField(max_length=100)