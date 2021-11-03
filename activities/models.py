from django.db import models
from django.contrib.auth.models import User


class Activities(models.Model):
    title = models.CharField(max_length=255, unique=True)
    points = models.IntegerField()


class Submissions(models.Model):
    grade = models.IntegerField(null=True)
    repo = models.CharField(max_length=511)
    user = models.ForeignKey("accounts.User", on_delete=models.DO_NOTHING)
    activity = models.ForeignKey(
        Activities, on_delete=models.DO_NOTHING, related_name="submissions"
    )
