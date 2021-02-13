from django.db import models

# Create your models here.
class User(models.Model):
  email = models.EmailField(max_length=254, unique=True, blank=False)
  password = models.CharField(max_length=50, blank=False)
  full_name = models.CharField(max_length=50, blank=False)
