# Generated by Django 5.0.7 on 2024-10-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "Home_Page",
            "0002_alter_book_detail_author_alter_book_detail_cover_url_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="book_detail",
            name="Publish_date",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
