# Generated by Django 4.1.6 on 2023-05-25 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="District",
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
                ("district_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Division",
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
                ("division_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
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
                ("region_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="State",
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
                ("state_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Zimmedar",
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
                ("name", models.CharField(max_length=200)),
                ("zehliHalqa", models.CharField(max_length=200)),
                ("alaqa", models.CharField(max_length=200)),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.district"
                    ),
                ),
                (
                    "division",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.division"
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.region"
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.state"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Report",
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
                ("zimmedar_name", models.CharField(default="", max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "zimmedari",
                    models.CharField(
                        choices=[
                            ("Alaqa Zimmedar Naik Aamal", "Alaqa Zimmedar Naik Aamal"),
                            (
                                "District Zimmedar Naik Aamal",
                                "District Zimmedar Naik Aamal",
                            ),
                            (
                                "Division Zimmedar Naik Aamal",
                                "Division Zimmedar Naik Aamal",
                            ),
                            ("State Zimmedar Naik Aamal", "State Zimmedar Naik Aamal"),
                            (
                                "Region Zimmedar Naik Aamal",
                                "Region Zimmedar Naik Aamal",
                            ),
                            ("Hind Zimmedar Naik Aamal", "Hind Zimmedar Naik Aamal"),
                            ("Other Zimmedar", "Other Zimmedar"),
                        ],
                        default="madinah",
                        max_length=50,
                    ),
                ),
                ("alaqa", models.CharField(max_length=100)),
                ("taqseem", models.BigIntegerField(max_length=100000)),
                ("wusool", models.BigIntegerField(max_length=100000)),
                ("islaheaamal_ijtima_maqam", models.BigIntegerField(max_length=10000)),
                (
                    "islaheaamal_ijtima_shuraqa",
                    models.BigIntegerField(max_length=10000),
                ),
                ("tahajjud_ijtima_maqam", models.BigIntegerField(max_length=10000)),
                ("tahajjud_ijtima_shuraqa", models.BigIntegerField(max_length=10000)),
                ("sehri_ijtima_maqam", models.BigIntegerField(max_length=10000)),
                ("sehri_ijtima_shuraqa", models.BigIntegerField(max_length=10000)),
                ("mehboob_e_attar", models.BigIntegerField(max_length=10000)),
                ("yaumequfle_madinah", models.BigIntegerField(max_length=10000)),
                (
                    "haftawar_ijtima_main_raat_guzarne_wale_Shuraqa",
                    models.BigIntegerField(max_length=100000),
                ),
                (
                    "disrict",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.district"
                    ),
                ),
                (
                    "division",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.division"
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.region"
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.state"
                    ),
                ),
                (
                    "zimmedar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]