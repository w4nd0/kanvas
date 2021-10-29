from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    course = models.ForeignKey("courses.Courses" , on_delete=models.DO_NOTHING)