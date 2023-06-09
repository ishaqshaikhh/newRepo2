# Generated by Django 4.2.1 on 2023-06-01 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "app",
            "0004_rename_yaumequfle_madinah_report_yaumequfle_madinah_maqam_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="haftawar_ijtima_main_raat_guzarne_wale_Shuraqa",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="haftawar_ijtima_main_raat_guzarne_wale_maqam",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="islaheaamal_ijtima_maqam",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="islaheaamal_ijtima_shuraqa",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="mehboob_e_attar",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="sehri_ijtima_maqam",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="sehri_ijtima_shuraqa",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="tahajjud_ijtima_maqam",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="tahajjud_ijtima_shuraqa",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="taqseem",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="wusool",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="yaumequfle_madinah_maqam",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="yaumequfle_madinah_shuraqa",
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]
