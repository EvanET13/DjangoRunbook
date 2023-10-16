# Generated by Django 4.2.3 on 2023-10-13 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_alter_site_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='battery',
            fields=[
                ('battery_id', models.IntegerField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='Battery ID')),
                ('battery_name', models.CharField(default=None, max_length=100, verbose_name='Battery Name')),
                ('battery_serial', models.CharField(blank=True, default=None, max_length=50, verbose_name='Battery Serial')),
                ('battery_install_month', models.SmallIntegerField(default=None, verbose_name='Battery Install Month')),
                ('battery_install_year', models.SmallIntegerField(default=None, verbose_name='Battery Install Year')),
                ('battery_count', models.SmallIntegerField(default=None, verbose_name='Battery Count')),
                ('battery_type', models.CharField(default=None, max_length=50, verbose_name='Battery Type')),
                ('battery_site_id', models.SmallIntegerField(default=None, verbose_name='Battery Site ID')),
                ('battery_notes', models.TextField(default=None, null=True, verbose_name='Battery Notes')),
            ],
            options={
                'db_table': 'battery',
            },
        ),
        migrations.CreateModel(
            name='battery_contact_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery_id', models.SmallIntegerField(default=None)),
                ('battery_contact_id', models.SmallIntegerField(default=None)),
            ],
            options={
                'db_table': 'battery_contact_link',
            },
        ),
        migrations.CreateModel(
            name='battery_contact_list',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='Contact List ID')),
                ('battery_id', models.SmallIntegerField(default=None, verbose_name='Battery ID')),
                ('battery_contact_id', models.SmallIntegerField(default=None, verbose_name='Battery Contact ID')),
            ],
            options={
                'db_table': 'battery_contact_list',
            },
        ),
        migrations.CreateModel(
            name='battery_contacts',
            fields=[
                ('battery_contact_id', models.IntegerField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='Battery Contact ID')),
                ('battery_contact_first', models.CharField(default=None, max_length=100, verbose_name='Battery Contact First')),
                ('battery_contact_last', models.CharField(default=None, max_length=100, verbose_name='Battery Contact Last')),
                ('battery_contact_company', models.CharField(default=None, max_length=100, verbose_name='Battery Contact Company')),
                ('battery_contact_phone', models.CharField(default=None, max_length=30, verbose_name='Battery Contact Phone')),
                ('battery_contact_cell', models.CharField(blank=True, default=None, max_length=30, verbose_name='Battery Contact Cell')),
                ('battery_contact_email', models.CharField(blank=True, default=None, max_length=55, verbose_name='Battery Contact Email')),
                ('battery_contact_afterhours', models.CharField(choices=[('Unknown', 'Unknown'), ('Yes', 'Yes'), ('No', 'No')], default=None, max_length=30, verbose_name='Battery Contact After Hours')),
                ('battery_contact_notes', models.TextField(blank=True, default=None, null=True, verbose_name='Battery Contact Notes')),
            ],
            options={
                'db_table': 'battery_contacts',
            },
        ),
        migrations.CreateModel(
            name='battery_tested_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery_test_timestamp', models.TimeField(blank=True, default=None, help_text='YYYY/MM/DD hh:mm:ss', null=True, verbose_name='Battery Test Timestamp')),
                ('site_id', models.SmallIntegerField(default=None, verbose_name='Site ID')),
                ('battery_tested', models.CharField(default=None, max_length=30, verbose_name='What Batteries were Tested?')),
                ('battery_tested_by', models.CharField(default=None, max_length=100, verbose_name='Batteries Tested By')),
                ('battery_tested_notes', models.TextField(default=None, null=True, verbose_name='Battery Tested Notes')),
            ],
            options={
                'db_table': 'battery_tested_link',
            },
        ),
        migrations.CreateModel(
            name='generator',
            fields=[
                ('generator_id', models.IntegerField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='Generator ID')),
                ('generator_site_id', models.SmallIntegerField(default=None, verbose_name='Generator Site ID')),
                ('generator_install_date', models.DateField(blank=True, default=None, help_text='YYYY/MM/DD', verbose_name='Generator Install Date')),
                ('generator_type', models.CharField(choices=[('Cummins', 'Cummins'), ('Generac', 'Generac'), ('Relion', 'Relion'), ('None', 'None'), ('Unknown', 'Unknown')], default=None, max_length=30, verbose_name='Generator Type')),
                ('generator_fuel', models.CharField(default=None, max_length=20, null=True, verbose_name='Generator Fuel')),
                ('generator_notes', models.TextField(blank=True, default=None, null=True, verbose_name='Generator Notes')),
            ],
            options={
                'db_table': 'generator',
            },
        ),
        migrations.CreateModel(
            name='generator_contact_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generator_id', models.SmallIntegerField(default=None, verbose_name='Generator ID')),
                ('generator_contact_id', models.SmallIntegerField(default=None, verbose_name='Generator Contact ID')),
            ],
            options={
                'db_table': 'generator_contact_link',
            },
        ),
        migrations.CreateModel(
            name='generator_contact_list',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID')),
                ('generator_id', models.SmallIntegerField(default=None, verbose_name='Generator ID')),
                ('generator_contact_id', models.SmallIntegerField(default=None, verbose_name='Generator Contact ID')),
            ],
            options={
                'db_table': 'generator_contact_list',
            },
        ),
        migrations.CreateModel(
            name='generator_contacts',
            fields=[
                ('generator_contact_id', models.IntegerField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='Generator Contact ID')),
                ('generator_contact_first', models.CharField(default=None, max_length=100, verbose_name='Generator Contact First')),
                ('generator_contact_last', models.CharField(default=None, max_length=100, verbose_name='Generator Contact Last')),
                ('generator_contact_company', models.CharField(default=None, max_length=100, verbose_name='Generator Contact Company')),
                ('generator_contact_phone', models.CharField(default=None, max_length=30, verbose_name='Generator Contact Phone')),
                ('generator_contact_cell', models.CharField(blank=True, default=None, max_length=30, verbose_name='Generator Contact Cell')),
                ('generator_contact_email', models.CharField(default=None, max_length=55, verbose_name='Generator Contact Email')),
                ('generator_contact_afterhours', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], default=None, max_length=30, verbose_name='Generator Contact After Hours')),
                ('generator_contact_notes', models.TextField(blank=True, default=None, null=True, verbose_name='Generator Contact Notes')),
            ],
            options={
                'db_table': 'generator_contacts',
            },
        ),
        migrations.CreateModel(
            name='generator_service_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generator_service_timestamp', models.TimeField(blank=True, default=None, help_text='YYYY/MM/DDhh:mm:ss', verbose_name='Generator Service Timestamp')),
                ('generator_id', models.SmallIntegerField(default=None, verbose_name='Generator ID')),
                ('generator_last_serviced', models.DateField(blank=True, default=None, help_text='YYYY/MM/DD', verbose_name='Generator Last Serviced')),
                ('generator_service_by', models.CharField(default=None, max_length=100, verbose_name='Generator Service By')),
                ('generator_service_notes', models.TextField(blank=True, default=None, null=True, verbose_name='Generator Service Notes')),
            ],
            options={
                'db_table': 'generator_service_link',
            },
        ),
        migrations.CreateModel(
            name='generator_tested_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generator_test_timestamp', models.TimeField(blank=True, default=None, help_text='YYYY/MM/DDhh:mm:ss', verbose_name='Generator Tested Timestamp')),
                ('generator_id', models.SmallIntegerField(default=None, verbose_name='Generator ID')),
                ('generator_last_tested', models.DateField(blank=True, default=None, help_text='YYYY/MM/DD', verbose_name='Generator Last Tested')),
                ('generator_tested_by', models.CharField(default=None, max_length=100, verbose_name='Generator Tested By')),
                ('generator_tested_notes', models.TextField(blank=True, default=None, null=True, verbose_name='Generator Tested Notes')),
            ],
            options={
                'db_table': 'generator_tested_link',
            },
        ),
        migrations.CreateModel(
            name='hvac',
            fields=[
                ('hvac_id', models.IntegerField(auto_created=True, default=None, help_text='The ID of the HVAC', primary_key=True, serialize=False, verbose_name='HVAC ID')),
                ('hvac_name', models.CharField(default=None, help_text='The name of the HVAC', max_length=50, verbose_name='HVAC Name')),
                ('hvac_type', models.CharField(choices=[('Marvair Compac', 'Marvair Compac'), ('Baird Compac', 'Baird Compac'), ('Building Supplied', 'Building Supplied'), ('IQ 3/4 Ton', 'IQ 3/4 Ton'), ('IQ 1 Ton', 'IQ 1 Ton'), ('Unknown', 'Unknown')], default=None, help_text='The type of the HVAC', max_length=50, verbose_name='HVAC Type')),
                ('hvac_filter_type', models.CharField(choices=[('Small', 'Small'), ('Large', 'Large'), ('Unknown', 'Unknown')], default=None, help_text='The filter type of the HVAC', max_length=30, verbose_name='HVAC Filter Type')),
                ('hvac_install_date', models.DateField(blank=True, default=None, help_text='YYYY/MM/DD', verbose_name='HVAC Install Date')),
                ('hvac_serial', models.CharField(blank=True, default=None, help_text='The serial number of the HVAC', max_length=50, verbose_name='HVAC Serial')),
                ('hvac_service_id', models.SmallIntegerField(default=None, help_text='The service ID of the HVAC', verbose_name='HVAC Service ID')),
                ('hvac_site_id', models.SmallIntegerField(default=None, help_text='The site ID of the HVAC', verbose_name='HVAC Site ID')),
                ('hvac_in_service', models.CharField(choices=[('Unknown', 'Unknown'), ('Yes', 'Yes'), ('No', 'No')], default=None, help_text='Whether the HVAC is in service or not', max_length=30, verbose_name='HVAC In Service')),
                ('hvac_notes', models.TextField(blank=True, default=None, help_text='Additional notes about the HVAC', null=True, verbose_name='HVAC Notes')),
                ('hvac_contact_first', models.CharField(blank=True, default=None, help_text='The first name of the HVAC contact', max_length=100, verbose_name='HVAC Contact First')),
                ('hvac_contact_last', models.CharField(blank=True, default=None, help_text='The last name of the HVAC contact', max_length=100, verbose_name='HVAC Contact Last')),
                ('hvac_contact_company', models.CharField(blank=True, default=None, help_text='The company of the HVAC contact', max_length=255, verbose_name='HVAC Contact Company')),
                ('hvac_contact_phone', models.CharField(blank=True, default=None, help_text='The phone number of the HVAC contact', max_length=30, verbose_name='HVAC Contact Phone')),
                ('hvac_contact_cell', models.CharField(blank=True, default=None, help_text='The cell number of the HVAC contact', max_length=30, verbose_name='HVAC Contact Cell')),
                ('hvac_contact_email', models.CharField(blank=True, default=None, help_text='The email of the HVAC contact', max_length=55, verbose_name='HVAC Contact Email')),
                ('hvac_contact_afterhours', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=None, help_text='Whether the HVAC contact is available after hours', max_length=30, verbose_name='HVAC Contact After Hours')),
                ('hvac_contact_notes', models.TextField(blank=True, default=None, help_text='Additional notes about the HVAC contact', null=True, verbose_name='HVAC Contact Notes')),
            ],
            options={
                'db_table': 'hvac',
            },
        ),
        migrations.CreateModel(
            name='hvac_clean_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hvac_clean_timestamp', models.TimeField(blank=True, default=None, help_text='YYYY/MM/DDhh:mm:ss', verbose_name='HVAC Clean Timestamp')),
                ('hvac_id', models.SmallIntegerField(default=None, verbose_name='HVAC ID')),
                ('hvac_clean_by', models.CharField(default=None, max_length=100, verbose_name='HVAC Clean By')),
                ('hvac_clean_notes', models.TextField(default=None, null=True, verbose_name='HVAC Clean Notes')),
            ],
            options={
                'db_table': 'hvac_clean_link',
            },
        ),
        migrations.CreateModel(
            name='hvac_contacts',
            fields=[
                ('hvac_contact_id', models.IntegerField(auto_created=True, default=None, help_text='The ID of the HVAC contact', primary_key=True, serialize=False, verbose_name='HVAC Contact ID')),
                ('hvac_contact_first', models.CharField(default=None, help_text='The first name of the HVAC contact', max_length=100, verbose_name='HVAC Contact First Name')),
                ('hvac_contact_last', models.CharField(default=None, help_text='The last name of the HVAC contact', max_length=100, verbose_name='HVAC Contact Last Name')),
                ('hvac_contact_company', models.CharField(default=None, help_text='The company of the HVAC contact', max_length=100, verbose_name='HVAC Contact Company')),
                ('hvac_contact_phone', models.CharField(default=None, help_text='The phone number of the HVAC contact', max_length=30, verbose_name='HVAC Contact Phone')),
                ('hvac_contact_cell', models.CharField(default=None, help_text='The cell number of the HVAC contact', max_length=30, verbose_name='HVAC Contact Cell')),
                ('hvac_contact_email', models.CharField(default=None, help_text='The email of the HVAC contact', max_length=55, verbose_name='HVAC Contact Email')),
                ('hvac_contact_afterhours', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], default=None, help_text='Whether the HVAC contact is available after hours', max_length=30, verbose_name='HVAC Contact After Hours')),
                ('hvac_contact_notes', models.TextField(default=None, help_text='Additional notes about the HVAC contact', null=True, verbose_name='HVAC Contact Notes')),
            ],
            options={
                'db_table': 'hvac_contacts',
            },
        ),
        migrations.CreateModel(
            name='hvac_service_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hvac_service_timestamp', models.TimeField(blank=True, default=None, help_text='YYYY/MM/DDhh:mm:ss', verbose_name='HVAC Service Timestamp')),
                ('hvac_id', models.SmallIntegerField(default=None, help_text='The ID of the HVAC', verbose_name='HVAC ID')),
                ('hvac_service_by', models.CharField(default=None, help_text='The name of the HVAC servicer', max_length=50, verbose_name='HVAC Service By')),
                ('hvac_service_notes', models.TextField(blank=True, default=None, help_text='Additional notes about the HVAC service', null=True, verbose_name='HVAC Service Notes')),
            ],
            options={
                'db_table': 'hvac_service_link',
            },
        ),
        migrations.CreateModel(
            name='hvac_temp_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hvac_temp_timestamp', models.TimeField(blank=True, default=None, help_text='YYYY/MM/DDhh:mm:ss')),
                ('hvac_id', models.SmallIntegerField(default=None)),
                ('hvac_temp_in', models.SmallIntegerField(default=None)),
                ('hvac_temp_out', models.SmallIntegerField(default=None)),
                ('hvac_temp_outside', models.SmallIntegerField(default=None)),
                ('hvac_temp_notes', models.TextField(default=None, null=True)),
            ],
            options={
                'db_table': 'hvac_temp_link',
            },
        ),
        migrations.CreateModel(
            name='site_access',
            fields=[
                ('site_access_id', models.IntegerField(auto_created=True, default=None, help_text='The ID of the site access.', primary_key=True, serialize=False, verbose_name='Site Access ID')),
                ('site_access_keys', models.CharField(choices=[('Physical Key', 'Physical Key'), ('Key Card/Fob', 'Key Card/Fob')], default=None, help_text='The type of keys used for site access.', max_length=50, verbose_name='Site Access Keys')),
                ('site_access_alarm_code', models.CharField(default=None, help_text='The alarm code for site access.', max_length=20, null=True, verbose_name='Site Access Alarm Code')),
                ('site_access_door_code', models.CharField(default=None, help_text='The door code for site access.', max_length=20, null=True, verbose_name='Site Access Door Code')),
                ('site_access_physical_key', models.CharField(choices=[('CVIN', 'CVIN'), ('From Lockbox', 'From Lockbox')], default=None, help_text='The type of physical key used for site access.', max_length=30, verbose_name='Site Access Physical Key')),
                ('site_access_physical_key_location', models.CharField(default=None, help_text='The location of the physical key for site access.', max_length=100, null=True, verbose_name='Site Access Physical Key Location')),
                ('site_access_rack_code', models.CharField(default=None, help_text='The rack code for site access.', max_length=20, null=True, verbose_name='Site Access Rack Code')),
                ('site_access_gate_code', models.CharField(default=None, help_text='The gate code for site access.', max_length=20, null=True, verbose_name='Site Access Gate Code')),
                ('site_access_additional_access_notes', models.TextField(default=None, help_text='Additional notes for site access.', null=True, verbose_name='Additional Access Notes')),
                ('site_access_additional_access_code', models.CharField(default=None, help_text='Additional access code for site access.', max_length=50, null=True, verbose_name='Site Access Additional Access Code')),
                ('site_access_notes', models.TextField(default=None, help_text='Notes for site access.', null=True, verbose_name='Site Access Notes')),
            ],
            options={
                'db_table': 'site_access',
            },
        ),
        migrations.CreateModel(
            name='site_access_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.SmallIntegerField(default=None, verbose_name='Site ID')),
                ('site_access_id', models.SmallIntegerField(default=None, verbose_name='Site Access ID')),
            ],
            options={
                'db_table': 'site_access_link',
            },
        ),
        migrations.CreateModel(
            name='site_contact_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.SmallIntegerField(default=None, verbose_name='Site ID')),
                ('contact_id', models.SmallIntegerField(default=None, verbose_name='Contact ID')),
            ],
            options={
                'db_table': 'site_contact_link',
            },
        ),
        migrations.CreateModel(
            name='site_distance',
            fields=[
                ('site_distance_id', models.IntegerField(auto_created=True, default=None, help_text='Unique identifier for the site distance', primary_key=True, serialize=False, verbose_name='Site Distance ID')),
                ('site_distance_circuit_id', models.CharField(default=None, help_text='Identifier for the circuit associated with the site distance', max_length=100, null=True, verbose_name='Site Distance Circuit ID')),
                ('site_distance_wavelength', models.CharField(default=None, help_text='Wavelength of the site distance', max_length=100, null=True, verbose_name='Site Distance Wavelength')),
                ('site_distance_frequency', models.CharField(default=None, help_text='Frequency of the site distance', max_length=100, null=True, verbose_name='Site Distance Frequency')),
                ('site_distance_provider', models.CharField(default=None, help_text='Provider of the site distance', max_length=100, null=True, verbose_name='Site Distance Provider')),
                ('site_distance_provider_phone', models.CharField(default=None, help_text='Phone number of the provider', max_length=50, null=True, verbose_name='Site Distance Provider Phone')),
                ('site_distance_provider_email', models.CharField(default=None, help_text='Email of the provider', max_length=55, null=True, verbose_name='Site Distance Provider Email')),
                ('site_distance', models.CharField(default=None, help_text='Distance between sites', max_length=20, null=True, verbose_name='Site Distance')),
                ('site_distance_site_id', models.SmallIntegerField(default=None, help_text='Identifier for the site associated with the site distance', verbose_name='Site Distance Site ID')),
                ('site_distance_endpoint_site_id', models.SmallIntegerField(default=None, help_text='Identifier for the endpoint site associated with the site distance', verbose_name='Site Distance Endpoint Site ID')),
                ('site_distance_provider_circuit_id', models.CharField(default=None, help_text='Identifier for the provider circuit associated with the site distance', max_length=50, null=True, verbose_name='Site Distance Provider Circuit ID')),
            ],
            options={
                'db_table': 'site_distance',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, default=None, help_text='Identifier for the user', primary_key=True, serialize=False, verbose_name='User ID')),
                ('username', models.CharField(default=None, help_text='Username of the user', max_length=50, null=True, verbose_name='Username')),
                ('password', models.CharField(default=None, help_text='Password of the user', max_length=50, null=True, verbose_name='Password')),
                ('user_first', models.CharField(default=None, help_text='First name of the user', max_length=50, null=True, verbose_name='First Name')),
                ('user_last', models.CharField(default=None, help_text='Last name of the user', max_length=50, null=True, verbose_name='Last Name')),
                ('user_phone', models.CharField(default=None, help_text='Phone number of the user', max_length=30, null=True, verbose_name='Phone')),
                ('user_phone_ext', models.CharField(default=None, help_text='Phone extension of the user', max_length=10, null=True, verbose_name='Phone Extension')),
                ('user_cell', models.CharField(default=None, help_text='Cell number of the user', max_length=30, null=True, verbose_name='Cell')),
                ('user_email', models.CharField(default=None, help_text='Email address of the user', max_length=55, null=True, verbose_name='Email')),
                ('user_notes', models.TextField(default=None, help_text='Additional notes about the user', null=True, verbose_name='Notes')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.RemoveField(
            model_name='site',
            name='site_access_id',
        ),
        migrations.AddField(
            model_name='site',
            name='site_clli',
            field=models.CharField(blank=True, default=None, help_text='CLLI code for the site', max_length=50, verbose_name='Site CLLI'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_address',
            field=models.CharField(default=None, help_text='Address of the site', max_length=100, verbose_name='Site Address'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_agent',
            field=models.CharField(blank=True, help_text='Agent information for the site', max_length=100, null=True, verbose_name='Site Agent'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_city',
            field=models.CharField(default=None, help_text='City of the site', max_length=65, verbose_name='Site City'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_emergency_power',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], default=None, help_text='Emergency power availability for the site', max_length=30, verbose_name='Site Emergency Power'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_generator',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], default=None, help_text='Generator availability for the site', max_length=30, verbose_name='Site Generator'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_id',
            field=models.IntegerField(auto_created=True, default=None, help_text='Unique identifier for the site', primary_key=True, serialize=False, verbose_name='Site ID'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_lat',
            field=models.DecimalField(decimal_places=10, default=None, help_text='Latitude coordinate of the site', max_digits=15, verbose_name='Site Latitude'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_long',
            field=models.DecimalField(decimal_places=10, default=None, help_text='Longitude coordinate of the site', max_digits=15, verbose_name='Site Longitude'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_name',
            field=models.CharField(default=None, help_text='Name of the site', max_length=100, verbose_name='Site Name'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_notes',
            field=models.TextField(blank=True, default=None, help_text='Additional notes for the site', null=True, verbose_name='Site Notes'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_power',
            field=models.CharField(help_text='Power information for the site', max_length=100, null=True, verbose_name='Site Power'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_power_account',
            field=models.CharField(blank=True, help_text='Power account information for the site', max_length=100, null=True, verbose_name='Site Power Account'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_short_name',
            field=models.CharField(default=None, help_text='Short name for the site', max_length=50, null=True, verbose_name='Site Short Name'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_state',
            field=models.CharField(default=None, help_text='State of the site', max_length=30, verbose_name='Site State'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_type',
            field=models.CharField(choices=[('Shelter - Owned', 'Shelter - Owned'), ('Shelter - Leased', 'Shelter - Leased'), ('Outside Cabinet', 'Outside Cabinet'), ('Colocation/Rackspace - Leased', 'Colocation/Rackspace - Leased'), ('Room/Office Space - Leased', 'Room/Office Space - Leased'), ('Site Notification', 'Site Notification')], default=None, help_text='Type of the site', max_length=100, verbose_name='Site Type'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_zip',
            field=models.IntegerField(default=None, help_text='ZIP code of the site', verbose_name='Site ZIP'),
        ),
        migrations.AlterModelTable(
            name='site',
            table='site',
        ),
        migrations.CreateModel(
            name='relion',
            fields=[
                ('relion_id', models.IntegerField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='Relion ID')),
                ('relion_site_name', models.CharField(default=None, max_length=100, verbose_name='Relion Site Name')),
                ('relion_serial', models.CharField(blank=True, default=None, max_length=100, verbose_name='Relion Serial')),
                ('relion_tank_replacement', models.DateField(blank=True, help_text='YYYY/MM/DD', verbose_name='Relion Tank Replacement')),
                ('relion_curr_psi', models.SmallIntegerField(default=None, verbose_name='Relion Current PSI')),
                ('relion_curr_psi_date', models.DateField(blank=True, help_text='YYYY/MM/DD', verbose_name='Relion Current PSI Date')),
                ('relion_prev_psi', models.SmallIntegerField(default=None, verbose_name='Relion Previous PSI')),
                ('relion_prev_psi_date', models.DateField(blank=True, help_text='YYYY/MM/DD', verbose_name='Relion Previous PSI Date')),
                ('relion_tank_contents', models.CharField(default=None, max_length=100, verbose_name='Relion Tank Contents')),
                ('relion_tank_size', models.SmallIntegerField(default=None, verbose_name='Relion Tank Size')),
                ('relion_tank_qty', models.SmallIntegerField(default=None, verbose_name='Relion Tank Quantity')),
                ('relion_notes', models.TextField(default=None, null=True, verbose_name='Relion Notes')),
                ('relion_contact_company', models.CharField(default=None, max_length=100, verbose_name='Relion Contact Company')),
                ('relion_contact_number', models.CharField(default=None, max_length=100, verbose_name='Relion Contact Number')),
                ('relion_account_number', models.CharField(default=None, max_length=100, verbose_name='Relion Account Number')),
                ('relion_site', models.ForeignKey(db_column='relion_site', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relion_site', to='catalog.site', verbose_name='Relion Site ID')),
            ],
            options={
                'db_table': 'relion',
            },
        ),
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('contact_id', models.IntegerField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='Contact ID')),
                ('contact_first', models.CharField(blank=True, default=None, max_length=100, verbose_name='Contact First')),
                ('contact_last', models.CharField(blank=True, default=None, max_length=100, verbose_name='Contact Last')),
                ('contact_phone', models.CharField(default=None, max_length=30, verbose_name='Contact Phone')),
                ('contact_ext', models.CharField(blank=True, default=None, max_length=30, verbose_name='Contact Ext')),
                ('contact_cell', models.CharField(blank=True, default=None, max_length=30, verbose_name='Contact Cell')),
                ('contact_email', models.CharField(default=None, max_length=50, verbose_name='Contact Email')),
                ('contact_afterhours', models.CharField(choices=[('Unknown', 'Unknown'), ('Yes', 'Yes'), ('No', 'No')], default=None, max_length=30, verbose_name='Contact After Hours')),
                ('contact_notes', models.TextField(blank=True, default=None, null=True, verbose_name='Contact Notes')),
                ('contact_247_name', models.CharField(blank=True, default=None, max_length=100, verbose_name='Contact 24/7 Name')),
                ('contact_247_phone', models.CharField(blank=True, default=None, max_length=30, verbose_name='Contact 24/7 Phone')),
                ('contact_247_email', models.CharField(blank=True, default=None, max_length=50, verbose_name='Contact 24/7 Email')),
                ('contact_247_notes', models.TextField(blank=True, default=None, null=True, verbose_name='Contact 24/7 Notes')),
                ('contact_site_id', models.ForeignKey(db_column='contact_site_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='catalog.site', verbose_name='Contact Site ID')),
            ],
            options={
                'db_table': 'contacts',
            },
        ),
    ]
