# Generated by Django 3.2.8 on 2021-11-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0005_alter_submissions_repo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submissions",
            name="grade",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="submissions",
            name="repo",
            field=models.CharField(max_length=511),
        ),
    ]
