# Generated by Django 4.1 on 2022-08-27 10:57
import django.db.models.deletion
import versatileimagefield.fields
from core.helpers import get_fixture
from django.db import migrations
from django.db import models


def load_fixture(apps, schema_editor):
    fixture_file = get_fixture("bot.json", "bot")

    fixture = open(fixture_file, "rb")
    from django.core import serializers

    objects = serializers.deserialize("json", fixture, ignorenonexistent=True)
    for obj in objects:
        obj.save()
    fixture.close()


def unload_fixture(apps, schema_editor):
    "Brutally deleting all entries for this model..."

    chat_text = apps.get_model("bot", "ChatText")
    chat_text.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatText",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(help_text="name of text", max_length=200)),
                ("text", models.TextField(help_text="text for chat")),
            ],
            options={
                "verbose_name": "Chat text",
                "verbose_name_plural": "Chat text",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("user_id", models.IntegerField(help_text="telegram user id", unique=True)),
                (
                    "username",
                    models.CharField(
                        blank=True, help_text="telegram user name", max_length=150, null=True, unique=True
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, help_text="telegram user name", max_length=30, null=True, unique=True),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, help_text="telegram user name", max_length=30, null=True, unique=True),
                ),
                (
                    "photo",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, help_text="telegram first photo", null=True, upload_to="images"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="queryresult",
            name="query",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, related_name="results", to="bot.searchquery"
            ),
        ),
        migrations.CreateModel(
            name="UserChat",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(default="", help_text="telegram chat name", max_length=150)),
                (
                    "user",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, related_name="chats", to="bot.user"
                    ),
                ),
            ],
            options={
                "verbose_name": "User Chat",
                "verbose_name_plural": "User Chat",
            },
        ),
        migrations.AddField(
            model_name="searchquery",
            name="chat",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, related_name="queries", to="bot.userchat"
            ),
        ),
        migrations.AddField(
            model_name="searchquery",
            name="user",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, related_name="queries", to="bot.user"
            ),
        ),
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]