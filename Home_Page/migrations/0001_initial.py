# Generated by Django 5.0.7 on 2024-10-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book_Detail",
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
                ("Title", models.CharField(max_length=400)),
                ("Author", models.CharField(max_length=200)),
                ("Genre", models.CharField(max_length=50)),
                ("Description", models.CharField(max_length=8000)),
                ("Publish_date", models.DateField()),
                ("Cover_url", models.CharField(max_length=300)),
            ],
        ),
    ]
