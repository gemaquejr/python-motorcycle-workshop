# Generated by Django 5.0.3 on 2024-09-09 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("mecanicos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TipoConserto",
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
                ("tempo_estimado", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ConsertoDeMoto",
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
                ("moto_id", models.IntegerField(default=0)),
                ("complexidade_do_conserto", models.IntegerField()),
                ("tempo_real", models.IntegerField(blank=True, null=True)),
                ("data_entrada", models.DateField()),
                (
                    "mecanico",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mecanicos.mecanico",
                    ),
                ),
                (
                    "tipo_conserto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="consertos.tipoconserto",
                    ),
                ),
            ],
        ),
    ]
