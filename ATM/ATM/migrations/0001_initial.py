# Generated by Django 5.1.5 on 2025-02-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("card_num", models.TextField()),
                ("pin", models.TextField()),
                ("S_account", models.TextField()),
                ("S_balance", models.TextField()),
                ("D_account", models.TextField()),
                ("D_balance", models.TextField()),
            ],
        ),
    ]
