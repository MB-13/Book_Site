# Generated by Django 5.0.7 on 2024-10-20 14:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Home_Page", "0005_book_detail_rating_book_detail_rating_count"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book_detail",
            name="Genre",
        ),
    ]
