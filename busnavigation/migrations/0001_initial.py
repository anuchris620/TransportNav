# Generated by Django 4.1.5 on 2024-05-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Stops_time",
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
                ("Routes", models.CharField(max_length=200)),
                ("time1", models.CharField(max_length=200)),
                ("time2", models.CharField(max_length=200)),
                ("time3", models.CharField(max_length=200)),
                ("time4", models.CharField(max_length=200)),
                ("time5", models.CharField(blank=True, max_length=200)),
                ("time6", models.CharField(blank=True, max_length=200)),
                ("time7", models.CharField(blank=True, max_length=200)),
                ("time8", models.CharField(blank=True, max_length=200)),
                ("time9", models.CharField(blank=True, max_length=200)),
                ("time10", models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
