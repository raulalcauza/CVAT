# Generated by Django 4.2.11 on 2024-06-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("engine", "0086_alter_data_consensus_job_per_segment"),
    ]

    operations = [
        migrations.AddField(
            model_name="data",
            name="agreement_score_threshold",
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="data",
            name="consensus_job_per_segment",
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]