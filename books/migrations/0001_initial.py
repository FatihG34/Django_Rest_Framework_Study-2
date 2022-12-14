# Generated by Django 4.1.1 on 2022-09-28 06:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("definition", models.TextField(blank=True, null=True)),
                ("createion_date", models.DateTimeField()),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("published_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("comments_owner", models.CharField(max_length=255)),
                ("comment", models.TextField(blank=True, null=True)),
                ("createion_date", models.DateTimeField()),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "rating",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator,
                            django.core.validators.MaxValueValidator,
                        ]
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="commnets",
                        to="books.book",
                    ),
                ),
            ],
        ),
    ]
