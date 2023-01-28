# Generated by Django 2.1.1 on 2021-12-02 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acrpapp', '0011_alter_applicant_design_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designapp',
            name='design_area',
            field=models.CharField(choices=[('AE', 'Airport Environmental Interactions'), ('AM', 'Airport Management and Planning'), ('AO', 'Airport Operations and Maintenance'), ('RS', 'Runway Safety/Runway Incursions/Runway Excursions Including Aprons, Ramps, and Taxiways')], max_length=3),
        ),
        migrations.AlterField(
            model_name='designapp',
            name='title',
            field=models.CharField(default='', max_length=300),
        ),
    ]