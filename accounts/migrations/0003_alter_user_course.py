# Generated by Django 3.2.8 on 2021-10-29 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
        ("accounts", "0002_alter_user_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="course",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="users",
                to="courses.courses",
            ),
        ),
    ]
