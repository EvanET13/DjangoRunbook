# Generated by Django 4.2.3 on 2023-07-27 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_site_hvac_name_hvactype_hvac_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HVACType',
            new_name='HVAC_Type',
        ),
    ]
