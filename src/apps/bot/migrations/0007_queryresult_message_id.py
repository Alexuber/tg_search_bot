# Generated by Django 4.1 on 2022-08-29 14:12
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0006_remove_queryresult_from_user_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="queryresult",
            name="message_id",
            field=models.IntegerField(default=0, help_text="message id"),
            preserve_default=False,
        ),
    ]