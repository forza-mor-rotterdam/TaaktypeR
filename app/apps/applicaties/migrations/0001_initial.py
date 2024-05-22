# Generated by Django 3.2.19 on 2023-06-29 13:49

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("aliassen", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Applicatie",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("aangemaakt_op", models.DateTimeField(auto_now_add=True)),
                ("aangepast_op", models.DateTimeField(auto_now=True)),
                ("naam", models.CharField(default="Applicatie", max_length=100)),
                ("basis_url", models.URLField(blank=True, null=True)),
                (
                    "applicatie_gebruiker_naam",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "applicatie_gebruiker_wachtwoord",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("taaktypes", models.JSONField(blank=True, default=list, null=True)),
                (
                    "gebruiker",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="applicaties_voor_gebruiker",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "onderwerpen",
                    models.ManyToManyField(
                        blank=True,
                        related_name="applicaties_voor_onderwerpen",
                        to="aliassen.OnderwerpAlias",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]