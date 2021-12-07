from django.db import models

# Create your models here.
class Resume(models.Model):
    experiece = models.TextField(max_length=400)
    skills = models.TextField(max_length=100)