from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=255)
    users = models.CharField(max_length=255)
