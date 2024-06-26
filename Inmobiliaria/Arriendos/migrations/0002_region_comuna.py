# Generated by Django 5.0.6 on 2024-05-25 02:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Arriendos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Region",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Comuna",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=50)),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comuna_region",
                        to="Arriendos.region",
                    ),
                ),
            ],
        ),
    ]
