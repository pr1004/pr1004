from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=254, null=False, blank=False)
  content = models.TextField(null=False, blank=False)
  created_at = models.DateField(auto_now = True, blank=False)
  updated_at = models.DateField(auto_now_add = True, blank=False)