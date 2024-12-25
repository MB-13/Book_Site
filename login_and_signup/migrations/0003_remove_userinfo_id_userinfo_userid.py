# Generated by Django 5.0.7 on 2024-12-17 18:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login_and_signup", "0002_rename_emailadderss_userinfo_emailaddress"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userinfo",
            name="id",
        ),
        migrations.AddField(
            model_name="userinfo",
            name="userId",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]