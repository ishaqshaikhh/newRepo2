# Generated by Django 4.1.6 on 2023-05-25 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="district",
            name="division_namef",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="app.division",
            ),
        ),
        migrations.AddField(
            model_name="division",
            name="state_namef",
            field=models.ForeignKey(
                default="", on_delete=django.db.models.deletion.CASCADE, to="app.state"
            ),
        ),
        migrations.AddField(
            model_name="state",
            name="region_namef",
            field=models.ForeignKey(
                default="", on_delete=django.db.models.deletion.CASCADE, to="app.region"
            ),
        ),
    ]