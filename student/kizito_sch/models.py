from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=254, unique=True, blank=True)
    password = models.CharField(max_length=254)
    usename = models.CharField(max_length=254)

class Courses(models.Model):
    course_name = models.CharField(max_length=254)
    course_image = models.CharField(max_length=254)
    course_description = models.TextField()