# Generated by Django 4.1.1 on 2022-09-29 10:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_alter_comment_book"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="createion_date",
        ),
        migrations.AddField(
            model_name="comment",
            name="creation_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]