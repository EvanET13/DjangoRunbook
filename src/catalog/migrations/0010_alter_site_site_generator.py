# Generated by Django 4.2.3 on 2023-07-31 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_site_site_emergency_power_delete_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='site_generator',
            field=models.CharField(help_text='Yes, no, or uknown', max_length=10, null=True),
        ),
    ]
