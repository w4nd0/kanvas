from django.db import models
from django.contrib.auth.models import User
class ModelCourses(models.Model):
    name = models.CharField(max_length=255)
