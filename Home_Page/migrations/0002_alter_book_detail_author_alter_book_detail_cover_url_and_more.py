# Generated by Django 5.0.7 on 2024-10-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home_Page", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book_detail",
            name="Author",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="book_detail",
            name="Cover_url",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="book_detail",
            name="Description",
            field=models.CharField(max_length=8000, null=True),
        ),
        migrations.AlterField(
            model_name="book_detail",
            name="Genre",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="book_detail",
            name="Publish_date",
            field=models.DateField(null=True),
        ),
    ]
