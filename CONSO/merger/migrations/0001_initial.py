# Generated by Django 4.2.11 on 2024-03-19 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MergeRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file1", models.FileField(upload_to="uploads/")),
                ("file2", models.FileField(upload_to="uploads/")),
            ],
        ),
    ]
