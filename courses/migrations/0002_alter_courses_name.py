# Generated by Django 3.2.8 on 2021-10-29 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courses",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
