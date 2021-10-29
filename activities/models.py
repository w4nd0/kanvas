from django.db import models
from django.contrib.auth.models import User

class Activities(models.Model):
    name = models.CharField(max_length=255)
    points = models.IntegerField()

class Submissions(models.Model):
    grade = models.IntegerField()
    repo = models.CharField(max_length=511)
    user = models.ForeignKey("accounts.User", on_delete=models.DO_NOTHING)
    activity =  models.ForeignKey("activities.Activities", on_delete=models.DO_NOTHING)
