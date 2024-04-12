# Generated by Django 4.2.11 on 2024-04-12 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="trainer", name="availability",),
        migrations.CreateModel(
            name="TrainerAvailiblity",
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
                (
                    "day_of_week",
                    models.IntegerField(
                        choices=[
                            (0, "Sunday"),
                            (1, "Monday"),
                            (2, "Tuesday"),
                            (3, "Wednesday"),
                            (4, "Thursday"),
                            (5, "Friday"),
                            (6, "Saturday"),
                        ]
                    ),
                ),
                ("check_in", models.TimeField()),
                ("check_out", models.TimeField()),
                (
                    "trainer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="availabilities",
                        to="myapp.trainer",
                    ),
                ),
            ],
        ),
    ]
