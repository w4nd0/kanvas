# Generated by Django 3.2.8 on 2021-11-02 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0004_alter_submissions_activity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submissions",
            name="repo",
            field=models.CharField(max_length=511, null=True),
        ),
    ]
