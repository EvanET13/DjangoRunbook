from django.db import models
from django.forms import ModelForm 
from django.utils.translation import gettext_lazy as _



'''
# Create your models here.

class MyModelName(models.Model):
     """A typical class defining a model, derived from the Model class."""

     # Fields -- explanation below
         # --  A model can have an arbitrary number of fields, of any type — each one represents a column of data
         #     that we want to store in one of our database tables. Each database record (row) will consist of one of
         #     each field value
#-----------------------------------------------------------------------------------------------------------------------------------------------------#        
     my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')                                                             
         #     max_length=20 — States that the maximum length of a value in this field is 20 characters.
         #     help_text='Enter field documentation' — helpful text that may be displayed in a form to help users understand how the field is used.
     # The field name is used to refer to it in queries and templates. Fields also have a label, which is
     # specified using the verbose_name argument (with a default value of None). If verbose_name is not set,
     # the label is created from the field name by replacing any underscores with a space, and capitalizing
     # the first letter (for example, the field my_field_name would have a default label of My field name when used in forms).

################################################################------FIELD TYPES------################################################################
#   https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models#:~:text=options%20here.-,COMMON%20FIELD%20TYPES,-The%20following%20list  #
#######################################################################################################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------#        
'''
class battery(models.Model):
    battery_id = models.IntegerField(primary_key=True, null=False, default= None, auto_created=True, verbose_name='Battery ID')
    battery_name = models.CharField(max_length=100, null=False, default= None, verbose_name='Battery Name')
    battery_serial = models.CharField(max_length=50, null=False, default= None, blank=True, verbose_name='Battery Serial')
    battery_install_month = models.SmallIntegerField(null=False, default= None, verbose_name='Battery Install Month')
    battery_install_year = models.SmallIntegerField(null=False, default= None, verbose_name='Battery Install Year')
    battery_count = models.SmallIntegerField(null=False, default= None, verbose_name='Battery Count')
    battery_type = models.CharField(max_length=50, null=False, default= None, verbose_name='Battery Type')
    battery_site_id = models.SmallIntegerField(null=False, default= None, verbose_name='Battery Site ID') # add 'battery_site_id', to formBattery
    battery_notes = models.TextField(null=True, default= None,  verbose_name='Battery Notes')
    class Meta:
        db_table = 'battery'
    
    def __str__(self):
        return self.battery_name
            
class battery_contact_list(models.Model):
    id = models.IntegerField(primary_key=True, null=False, default= None, auto_created=True, verbose_name='Contact List ID')
    battery_id = models.SmallIntegerField(null=False, default= None, verbose_name='Battery ID')
    battery_contact_id = models.SmallIntegerField(null=False, default= None, verbose_name='Battery Contact ID')
    class Meta:
        db_table = 'battery_contact_list'
        
class battery_contacts(models.Model): #, forms.Form):
    battery_contact_id = models.IntegerField(primary_key=True, null=False, default= None, auto_created=True, verbose_name='Battery Contact ID')
    battery_contact_first = models.CharField(max_length=100, null=False, default= None, verbose_name='Battery Contact First')
    battery_contact_last = models.CharField(max_length=100, null=False, default= None, verbose_name='Battery Contact Last')
    battery_contact_company = models.CharField(max_length=100, null=False, default= None, verbose_name='Battery Contact Company')
    battery_contact_phone = models.CharField(max_length=30, null=False, default= None, verbose_name='Battery Contact Phone')
    battery_contact_cell = models.CharField(max_length=30, null=False, default= None, verbose_name='Battery Contact Cell', blank=True)
    battery_contact_email = models.CharField(max_length=55, null=False, default= None, verbose_name='Battery Contact Email', blank=True)
    # battery_contact_afterhours = forms.ChoiceField(choices=(('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')), default= None)
    battery_contact_afterhours = models.CharField(max_length=30,choices=(('Unknown', 'Unknown'), ('Yes', 'Yes'), ('No', 'No')), default= None, verbose_name='Battery Contact After Hours')
    battery_contact_notes = models.TextField(null=True, default= None, verbose_name='Battery Contact Notes', blank=True)
    class Meta:
        db_table = 'battery_contacts'
        
class battery_tested_link(models.Model):
    battery_test_timestamp = models.TimeField(auto_now_add=False, auto_now=False, blank=True, default= None, null=True, help_text= "YYYY/MM/DD hh:mm:ss", verbose_name='Battery Test Timestamp')
    site_id = models.SmallIntegerField(null=False, default= None, verbose_name='Site ID')
    battery_tested = models.CharField(max_length=30, null=False, default= None, verbose_name='What Batteries were Tested?')
    battery_tested_by = models.CharField(max_length=100, null=False, default= None, verbose_name='Batteries Tested By')
    battery_tested_notes = models.TextField(null=True, default= None, verbose_name='Battery Tested Notes')
    class Meta:
        db_table = 'battery_tested_link'

class battery_contact_link(models.Model):
    battery_id = models.SmallIntegerField(null=False, default= None)
    battery_contact_id = models.SmallIntegerField(null=False, default= None)
    class Meta:
        db_table = 'battery_contact_link'   
        
class relion(models.Model):
    relion_id = models.IntegerField(primary_key=True, null=False, default= None, auto_created=True, verbose_name='Relion ID')
    relion_site_name = models.CharField(max_length=100, null=False, default= None, verbose_name='Relion Site Name')
    relion_serial = models.CharField(max_length=100, null=False, default= None, verbose_name='Relion Serial', blank=True)
    relion_tank_replacement = models.DateField(help_text= "YYYY/MM/DD", auto_now_add=False, auto_now=False, blank=True, verbose_name='Relion Tank Replacement')
    relion_curr_psi = models.SmallIntegerField(null=False, default= None, verbose_name='Relion Current PSI')
    relion_curr_psi_date = models.DateField(help_text= "YYYY/MM/DD", auto_now_add=False, auto_now=False, blank=True, verbose_name='Relion Current PSI Date')
    relion_prev_psi = models.SmallIntegerField(null=False, default= None, verbose_name='Relion Previous PSI')
    relion_prev_psi_date = models.DateField(help_text= "YYYY/MM/DD", auto_now_add=False, auto_now=False, blank=True, verbose_name='Relion Previous PSI Date')
    relion_tank_contents = models.CharField(max_length=100, null=False, default= None, verbose_name='Relion Tank Contents')
    relion_tank_size = models.SmallIntegerField(null=False, default= None, verbose_name='Relion Tank Size')
    relion_tank_qty = models.SmallIntegerField(null=False, default= None, verbose_name='Relion Tank Quantity')
    relion_notes = models.TextField(null=True, default= None, verbose_name='Relion Notes')
    relion_site = models.ForeignKey('site', on_delete=models.CASCADE, null=True, default= None, verbose_name='Relion Site ID', related_name='relion_site', db_column='relion_site')
    relion_contact_company = models.CharField(max_length=100, null=False, default= None, verbose_name='Relion Contact Company')
    relion_contact_number = models.CharField(max_length=100, null=False, default= None, verbose_name='Relion Contact Number')
    relion_account_number = models.CharField(max_length=100, null=False, default= None, verbose_name='Relion Account Number')
    class Meta:
        db_table = 'relion' 
    
class generator(models.Model):
    generator_id = models.IntegerField(primary_key=True, null=False, default= None, auto_created=True, verbose_name='Generator ID')
    generator_site_id = models.SmallIntegerField(null=False, default= None, verbose_name='Generator Site ID')
    generator_install_date = models.DateField(null=False, default=None, help_text= "YYYY/MM/DD", auto_now_add=False, auto_now=False, blank=True, verbose_name='Generator Install Date')
    generator_type = models.CharField(max_length=30,choices=(('Cummins', 'Cummins'), ('Generac', 'Generac'), ('Relion', 'Relion'), ('None', 'None'), ('Unknown', 'Unknown')), default= None, verbose_name='Generator Type')
    generator_fuel = models.CharField(max_length=20, null= True, default= None, verbose_name='Generator Fuel')
    generator_notes = models.TextField(null=True, default= None, verbose_name='Generator Notes', blank=True)
    class Meta:
        db_table = 'generator'
        
class generator_contact_list(models.Model):
    id = models.IntegerField(primary_key=True, null=False, default=None, auto_created=True, verbose_name="ID")
    generator_id = models.SmallIntegerField(null=False, default=None, verbose_name="Generator ID")
    generator_contact_id = models.SmallIntegerField(null=False, default=None, verbose_name="Generator Contact ID")
    class Meta:
        db_table = 'generator_contact_list'

class generator_contact_link(models.Model):
    generator_id = models.SmallIntegerField(verbose_name='Generator ID', null=False, default=None)
    generator_contact_id = models.SmallIntegerField(verbose_name='Generator Contact ID', null=False, default=None)
    class Meta:
        db_table = 'generator_contact_link'
        
class generator_contacts(models.Model):
    generator_contact_id = models.IntegerField(primary_key=True, null=False, default= None, auto_created=True, verbose_name='Generator Contact ID')
    generator_contact_first = models.CharField(max_length=100, null=False, default= None, verbose_name='Generator Contact First')
    generator_contact_last = models.CharField(max_length=100, null=False, default= None, verbose_name='Generator Contact Last')
    generator_contact_company = models.CharField(max_length=100, null=False, default= None, verbose_name='Generator Contact Company')
    generator_contact_phone = models.CharField(max_length=30, null=False, default= None, verbose_name='Generator Contact Phone')
    generator_contact_cell = models.CharField(max_length=30, null=False, default= None, verbose_name='Generator Contact Cell', blank=True)
    generator_contact_email = models.CharField(max_length=55, null=False, default= None, verbose_name='Generator Contact Email')
    generator_contact_afterhours = models.CharField(max_length=30, choices=(('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')), default= None, verbose_name='Generator Contact After Hours')
    generator_contact_notes = models.TextField(null=True, default= None, verbose_name='Generator Contact Notes', blank=True)
    class Meta:
        db_table = 'generator_contacts' 
        
class generator_service_link(models.Model):
    generator_service_timestamp = models.TimeField(verbose_name="Generator Service Timestamp", null=False, default=None, auto_now_add=False, auto_now=False, blank=True, help_text="YYYY/MM/DD" "hh:mm:ss")
    generator_id = models.SmallIntegerField(verbose_name="Generator ID", null=False, default=None)
    generator_last_serviced = models.DateField(verbose_name="Generator Last Serviced", null=False, default=None, help_text="YYYY/MM/DD", auto_now_add=False, auto_now=False, blank=True)
    generator_service_by = models.CharField(verbose_name="Generator Service By", max_length=100, null=False, default=None)
    generator_service_notes = models.TextField(verbose_name="Generator Service Notes", null=True, default=None, blank=True)
    class Meta:
        db_table = 'generator_service_link'
        
class generator_tested_link(models.Model):
    generator_test_timestamp = models.TimeField(null=False, default=None, auto_now_add=False, auto_now=False, blank=True, help_text= "YYYY/MM/DD" "hh:mm:ss", verbose_name="Generator Tested Timestamp")
    generator_id = models.SmallIntegerField(null=False, default= None, verbose_name="Generator ID")
    generator_last_tested = models.DateField(null=False, default=None, help_text= "YYYY/MM/DD", auto_now_add=False, auto_now=False, blank=True, verbose_name="Generator Last Tested")
    generator_tested_by = models.CharField(max_length=100, null=False, default= None, verbose_name="Generator Tested By")
    generator_tested_notes = models.TextField(null=True, default= None, verbose_name="Generator Tested Notes", blank=True)
    class Meta:
        db_table = 'generator_tested_link' 

class hvac(models.Model):
    hvac_id = models.IntegerField(primary_key=True, null=False, default=None, auto_created=True, verbose_name="HVAC ID", help_text="The ID of the HVAC")
    hvac_name = models.CharField(max_length=50, null=False, default=None, verbose_name="HVAC Name", help_text="The name of the HVAC")
    hvac_type = models.CharField(max_length=50, choices=(('Marvair Compac', 'Marvair Compac'), ('Baird Compac', 'Baird Compac'), ('Building Supplied', 'Building Supplied'), ('IQ 3/4 Ton', 'IQ 3/4 Ton'), ('IQ 1 Ton', 'IQ 1 Ton'), ('Unknown', 'Unknown')), default=None, verbose_name="HVAC Type", help_text="The type of the HVAC")
    hvac_filter_type = models.CharField(max_length=30, choices=(('Small', 'Small'), ('Large', 'Large'), ('Unknown', 'Unknown')), default=None, verbose_name="HVAC Filter Type", help_text="The filter type of the HVAC")
    hvac_install_date = models.DateField(null=False, default=None, help_text="YYYY/MM/DD", auto_now_add=False, auto_now=False, blank=True, verbose_name="HVAC Install Date")
    hvac_serial = models.CharField(max_length=50, null=False, default=None, blank=True, verbose_name="HVAC Serial", help_text="The serial number of the HVAC")
    hvac_service_id = models.SmallIntegerField(null=False, default=None, verbose_name="HVAC Service ID", help_text="The service ID of the HVAC")
    hvac_site_id = models.SmallIntegerField(null=False, default=None, verbose_name="HVAC Site ID", help_text="The site ID of the HVAC")
    hvac_in_service = models.CharField(max_length=30, choices=(('Unknown', 'Unknown'), ('Yes', 'Yes'), ('No', 'No')), default=None, verbose_name="HVAC In Service", help_text="Whether the HVAC is in service or not")
    hvac_notes = models.TextField(null=True, default=None, blank=True, verbose_name="HVAC Notes", help_text="Additional notes about the HVAC")
    hvac_contact_first = models.CharField(max_length=100, null=False, default=None, blank=True, verbose_name="HVAC Contact First", help_text="The first name of the HVAC contact")
    hvac_contact_last = models.CharField(max_length=100, null=False, default=None, blank=True, verbose_name="HVAC Contact Last", help_text="The last name of the HVAC contact")
    hvac_contact_company = models.CharField(max_length=255, null=False, default=None, blank=True, verbose_name="HVAC Contact Company", help_text="The company of the HVAC contact")
    hvac_contact_phone = models.CharField(max_length=30, null=False, default=None, blank=True, verbose_name="HVAC Contact Phone", help_text="The phone number of the HVAC contact")
    hvac_contact_cell = models.CharField(max_length=30, null=False, default=None, blank=True, verbose_name="HVAC Contact Cell", help_text="The cell number of the HVAC contact")
    hvac_contact_email = models.CharField(max_length=55, null=False, default=None, blank=True, verbose_name="HVAC Contact Email", help_text="The email of the HVAC contact")
    hvac_contact_afterhours = models.CharField(max_length=30, choices=(('Yes', 'Yes'), ('No', 'No')), default=None, verbose_name="HVAC Contact After Hours", help_text="Whether the HVAC contact is available after hours")
    hvac_contact_notes = models.TextField(null=True, default= None, blank=True, verbose_name="HVAC Contact Notes", help_text="Additional notes about the HVAC contact")
    class Meta:
        db_table = 'hvac'
        
class hvac_clean_link(models.Model):
    hvac_clean_timestamp = models.TimeField(null=False, default=None, auto_now_add=False, auto_now=False, blank=True, help_text= "YYYY/MM/DD" "hh:mm:ss", verbose_name="HVAC Clean Timestamp")
    hvac_id = models.SmallIntegerField(null=False, default= None, verbose_name="HVAC ID")
    hvac_clean_by = models.CharField(max_length=100, null=False, default= None, verbose_name="HVAC Clean By")
    hvac_clean_notes = models.TextField(null=True, default= None, verbose_name="HVAC Clean Notes")
    class Meta:
        db_table = 'hvac_clean_link'   
        
class hvac_contacts(models.Model):
    hvac_contact_id = models.IntegerField(primary_key=True, null=False, default=None, auto_created=True, verbose_name='HVAC Contact ID', help_text='The ID of the HVAC contact')
    hvac_contact_first = models.CharField(max_length=100, null=False, default=None, verbose_name='HVAC Contact First Name', help_text='The first name of the HVAC contact')
    hvac_contact_last = models.CharField(max_length=100, null=False, default=None, verbose_name='HVAC Contact Last Name', help_text='The last name of the HVAC contact')
    hvac_contact_company = models.CharField(max_length=100, null=False,default=None,verbose_name='HVAC Contact Company',help_text='The company of the HVAC contact')
    hvac_contact_phone = models.CharField(max_length=30,null=False,default=None,verbose_name='HVAC Contact Phone',help_text='The phone number of the HVAC contact')
    hvac_contact_cell = models.CharField(max_length=30,null=False,default=None,verbose_name='HVAC Contact Cell',help_text='The cell number of the HVAC contact')
    hvac_contact_email = models.CharField(max_length=55,null=False,default=None,verbose_name='HVAC Contact Email',help_text='The email of the HVAC contact')
    hvac_contact_afterhours = models.CharField(max_length=30,choices=(('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')),default=None,verbose_name='HVAC Contact After Hours',help_text='Whether the HVAC contact is available after hours')
    hvac_contact_notes = models.TextField(null=True,default=None,verbose_name='HVAC Contact Notes',help_text='Additional notes about the HVAC contact')
    class Meta:
        db_table = 'hvac_contacts' 

class hvac_service_link(models.Model):
    hvac_service_timestamp = models.TimeField(null=False, default=None, auto_now_add=False, auto_now=False, blank=True, help_text= "YYYY/MM/DD" "hh:mm:ss", verbose_name="HVAC Service Timestamp")
    hvac_id = models.SmallIntegerField(null=False, default= None, verbose_name="HVAC ID", help_text="The ID of the HVAC")
    hvac_service_by = models.CharField(max_length=50, null=False, default= None, verbose_name="HVAC Service By", help_text="The name of the HVAC servicer")
    hvac_service_notes = models.TextField(null=True, default= None, blank=True, help_text= "Additional notes about the HVAC service", verbose_name="HVAC Service Notes")
    class Meta:
        db_table = 'hvac_service_link'

class hvac_temp_link(models.Model):
    hvac_temp_timestamp = models.TimeField(null=False, default=None, auto_now_add=False, auto_now=False, blank=True, help_text= "YYYY/MM/DD" "hh:mm:ss")
    hvac_id = models.SmallIntegerField(null=False, default= None)
    hvac_temp_in = models.SmallIntegerField(null=False, default= None)
    hvac_temp_out = models.SmallIntegerField(null=False, default= None)
    hvac_temp_outside = models.SmallIntegerField(null=False, default= None)
    hvac_temp_notes = models.TextField(null=True, default= None)
    class Meta:
        db_table = 'hvac_temp_link'
            
class site(models.Model):
    site_id = models.IntegerField(primary_key=True, null=False, default=None, auto_created=True, verbose_name='Site ID', help_text='Unique identifier for the site')
    site_clli = models.CharField(max_length=50, null=False, default=None, blank=True, verbose_name='Site CLLI', help_text='CLLI code for the site')
    site_short_name = models.CharField(max_length=50, null=True, default=None, verbose_name='Site Short Name', help_text='Short name for the site')
    site_name = models.CharField(max_length=100, null=False, default=None, verbose_name='Site Name', help_text='Name of the site')
    site_address = models.CharField(max_length=100, null=False, default=None, verbose_name='Site Address', help_text='Address of the site')
    site_city = models.CharField(max_length=65, null=False, default=None, verbose_name='Site City', help_text='City of the site')
    site_state = models.CharField(max_length=30, null=False, default=None, verbose_name='Site State', help_text='State of the site')
    site_zip = models.IntegerField(null=False, default=None, verbose_name='Site ZIP', help_text='ZIP code of the site')
    site_lat = models.DecimalField(max_digits=15, decimal_places=10, null=False, default=None, verbose_name='Site Latitude', help_text='Latitude coordinate of the site')
    site_long = models.DecimalField(max_digits=15, decimal_places=10, null=False, default=None, verbose_name='Site Longitude', help_text='Longitude coordinate of the site')
    site_power = models.CharField(max_length=100, null=True, verbose_name='Site Power', help_text='Power information for the site')
    site_agent = models.CharField(max_length=100, null=True, blank=True, verbose_name='Site Agent', help_text='Agent information for the site')
    site_power_account = models.CharField(max_length=100, null=True, blank=True, verbose_name='Site Power Account', help_text='Power account information for the site')
    site_type = models.CharField(max_length=100, choices=(('Shelter - Owned', 'Shelter - Owned'), ('Shelter - Leased', 'Shelter - Leased'), ('Outside Cabinet', 'Outside Cabinet'), ('Colocation/Rackspace - Leased', 'Colocation/Rackspace - Leased'), ('Room/Office Space - Leased', 'Room/Office Space - Leased'), ('Site Notification', 'Site Notification')), default=None, verbose_name='Site Type', help_text='Type of the site')
    site_emergency_power = models.CharField(max_length=30, choices=(('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')), default=None, verbose_name='Site Emergency Power', help_text='Emergency power availability for the site')
    site_generator = models.CharField(max_length=30, choices=(('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')), default=None, verbose_name='Site Generator', help_text='Generator availability for the site')
    site_notes = models.TextField(null=True, default=None, blank=True, verbose_name='Site Notes', help_text='Additional notes for the site')

    class Meta:
        db_table = "site"
    def __str__(self):
        return str(self.site_id) + " - " + self.site_name

class contacts(models.Model):
    contact_id = models.IntegerField(primary_key=True, null=False, default=None, auto_created=True, verbose_name='Contact ID')
    contact_first = models.CharField(max_length=100, null=False, default=None, verbose_name='Contact First', blank=True)
    contact_last = models.CharField(max_length=100, null=False, default=None, verbose_name='Contact Last', blank=True)
    contact_phone = models.CharField(max_length=30, null=False, default=None, verbose_name='Contact Phone')
    contact_ext = models.CharField(max_length=30, null=False, default=None, blank=True, verbose_name='Contact Ext')
    contact_cell = models.CharField(max_length=30, null=False, default=None, blank=True, verbose_name='Contact Cell')
    contact_email = models.CharField(max_length=50, null=False, default=None, verbose_name='Contact Email')
    contact_afterhours = models.CharField(max_length=30, choices=(('Unknown', 'Unknown'), ('Yes', 'Yes'), ('No', 'No')), default=None, verbose_name='Contact After Hours')
    contact_notes = models.TextField(null=True, default=None, blank=True, verbose_name='Contact Notes')
    contact_247_name = models.CharField(max_length=100, null=False, default=None, blank=True, verbose_name='Contact 24/7 Name')
    contact_247_phone = models.CharField(max_length=30, null=False, default=None, blank=True, verbose_name='Contact 24/7 Phone')
    contact_247_email = models.CharField(max_length=50, null=False, default=None, blank=True, verbose_name='Contact 24/7 Email')
    contact_247_notes = models.TextField(null=True, default=None, blank=True, verbose_name='Contact 24/7 Notes')
    # TODO: contact_site_id needs to be a foreign key having a relationship to site.site_id
    
    contact_site_id = models.ForeignKey(
        'site',  # Reference the 'site' model
        null=True,  # Allow NULL values
        on_delete=models.CASCADE,  # Delete the contact if the associated site is deleted
        default=None,  # Default value is None
        verbose_name='Contact Site ID',
        related_name='contacts',  # Optional: You can use this related_name for reverse lookups
        db_column='contact_site_id'
    )
    class Meta:
        db_table = 'contacts'
    def __str__(self):
        return str(self.contact_id) + " - " + self.contact_first + " " + self.contact_last
    
class site_access(models.Model):
    site_access_id = models.IntegerField(primary_key=True, null=False, default=None, auto_created=True, verbose_name="Site Access ID", help_text="The ID of the site access.")
    site_access_keys = models.CharField(max_length=50, choices=(('Physical Key', 'Physical Key'), ('Key Card/Fob', 'Key Card/Fob')), default=None, verbose_name="Site Access Keys", help_text="The type of keys used for site access.")
    site_access_alarm_code = models.CharField(max_length=20, null=True, default=None, verbose_name="Site Access Alarm Code", help_text="The alarm code for site access.")
    site_access_door_code = models.CharField(max_length=20, null=True, default=None, verbose_name="Site Access Door Code", help_text="The door code for site access.")
    site_access_physical_key = models.CharField(max_length=30, choices=(('CVIN', 'CVIN'), ('From Lockbox', 'From Lockbox')), default=None, verbose_name="Site Access Physical Key", help_text="The type of physical key used for site access.")
    site_access_physical_key_location = models.CharField(max_length=100, null=True, default=None, verbose_name="Site Access Physical Key Location", help_text="The location of the physical key for site access.")
    site_access_rack_code = models.CharField(max_length=20, null=True, default=None, verbose_name="Site Access Rack Code", help_text="The rack code for site access.")
    site_access_gate_code = models.CharField(max_length=20, null=True, default=None, verbose_name="Site Access Gate Code", help_text="The gate code for site access.")
    site_access_additional_access_notes = models.TextField(null=True, default=None, verbose_name="Additional Access Notes", help_text="Additional notes for site access.")
    site_access_additional_access_code = models.CharField(max_length=50, null=True, default=None, verbose_name="Site Access Additional Access Code", help_text="Additional access code for site access.")
    site_access_notes = models.TextField(null=True, default=None, verbose_name="Site Access Notes", help_text="Notes for site access.")
    class Meta:
        db_table = 'site_access'
        
class site_access_link(models.Model):
    site_id = models.SmallIntegerField(null=False, default= None, verbose_name="Site ID")
    site_access_id = models.SmallIntegerField(null=False, default= None, verbose_name="Site Access ID")
    class Meta:
        db_table = 'site_access_link' 
        
class site_contact_link(models.Model):
    site_id = models.SmallIntegerField(null=False, default= None, verbose_name="Site ID")
    contact_id = models.SmallIntegerField(null=False, default= None, verbose_name="Contact ID")
    class Meta:
        db_table = 'site_contact_link'

class site_distance(models.Model):
    site_distance_id = models.IntegerField(primary_key=True, null=False, default=None, auto_created=True, verbose_name="Site Distance ID", help_text="Unique identifier for the site distance")
    site_distance_circuit_id = models.CharField(max_length=100, null=True, default=None, verbose_name="Site Distance Circuit ID", help_text="Identifier for the circuit associated with the site distance")
    site_distance_wavelength = models.CharField(max_length=100, null=True, default=None, verbose_name="Site Distance Wavelength", help_text="Wavelength of the site distance")
    site_distance_frequency = models.CharField(max_length=100, null=True, default=None, verbose_name="Site Distance Frequency", help_text="Frequency of the site distance")
    site_distance_provider = models.CharField(max_length=100, null=True, default=None, verbose_name="Site Distance Provider", help_text="Provider of the site distance")
    site_distance_provider_phone = models.CharField(max_length=50, null=True, default=None, verbose_name="Site Distance Provider Phone", help_text="Phone number of the provider")
    site_distance_provider_email = models.CharField(max_length=55, null=True, default=None, verbose_name="Site Distance Provider Email", help_text="Email of the provider")
    site_distance = models.CharField(max_length=20, null=True, default=None, verbose_name="Site Distance", help_text="Distance between sites")
    site_distance_site_id = models.SmallIntegerField(null=False, default=None, verbose_name="Site Distance Site ID", help_text="Identifier for the site associated with the site distance")
    site_distance_endpoint_site_id = models.SmallIntegerField(null=False, default=None, verbose_name="Site Distance Endpoint Site ID", help_text="Identifier for the endpoint site associated with the site distance")
    site_distance_provider_circuit_id = models.CharField(max_length=50, null=True, default=None, verbose_name="Site Distance Provider Circuit ID", help_text="Identifier for the provider circuit associated with the site distance")
    class Meta:
        db_table = 'site_distance'
        
class users(models.Model):
    user_id = models.IntegerField(primary_key=True, null=False, default=None, auto_created=True, verbose_name="User ID", help_text="Identifier for the user")
    username = models.CharField(max_length=50, null=True, default=None, verbose_name="Username", help_text="Username of the user")
    password = models.CharField(max_length=50, null=True, default=None, verbose_name="Password", help_text="Password of the user")
    user_first = models.CharField(max_length=50, null=True, default=None, verbose_name="First Name", help_text="First name of the user")
    user_last = models.CharField(max_length=50, null=True, default=None, verbose_name="Last Name", help_text="Last name of the user")
    user_phone = models.CharField(max_length=30, null=True, default=None, verbose_name="Phone", help_text="Phone number of the user")
    user_phone_ext = models.CharField(max_length=10, null=True, default=None, verbose_name="Phone Extension", help_text="Phone extension of the user")
    user_cell = models.CharField(max_length=30, null=True, default=None, verbose_name="Cell", help_text="Cell number of the user")
    user_email = models.CharField(max_length=55, null=True, default=None, verbose_name="Email", help_text="Email address of the user")
    user_notes = models.TextField(null=True, default=None, verbose_name="Notes", help_text="Additional notes about the user")
    class Meta:
        db_table = 'users'


#---------------------------------------Forms---------------------------------------#      
class siteForm(ModelForm):
    class Meta:
        model = site
        fields = ['site_short_name', 'site_name', 
                  'site_address', 'site_city', 'site_state', 
                  'site_zip', 'site_lat', 'site_long', 'site_power', 'site_agent', 'site_type',
                  'site_power_account', 'site_emergency_power', 'site_generator', 'site_notes'
                ]

class batteryForm(ModelForm):
    class Meta:
        model = battery
        fields = ['battery_name', 'battery_serial', 'battery_install_month',
                  'battery_install_year', 'battery_count', 'battery_type', 
                  'battery_notes'
                ] # 'battery_runtime' was removed
        
class hvacForm(ModelForm):
    class Meta:
        model = hvac
        fields = ['hvac_name', 'hvac_type', 'hvac_filter_type', 
                  'hvac_install_date', 'hvac_serial', 'hvac_service_id',
                  'hvac_site_id', 'hvac_in_service', 'hvac_notes',
                  'hvac_contact_first', 'hvac_contact_last', 'hvac_contact_company',
                  'hvac_contact_phone', 'hvac_contact_cell', 'hvac_contact_email', 'hvac_contact_afterhours', 'hvac_contact_notes'
                ]

class relionForm(ModelForm):
    class Meta:
        model = relion
        fields = ['relion_site_name', 'relion_serial', 'relion_tank_replacement', 
                  'relion_curr_psi', 'relion_curr_psi_date', 'relion_prev_psi','relion_prev_psi_date',
                  'relion_tank_contents', 'relion_tank_size', 'relion_tank_qty', 'relion_notes', 
                  'relion_site', 'relion_contact_company', 'relion_contact_number', 'relion_account_number'
                ]    
        
class contactsForm(ModelForm):
    class Meta:
        model = contacts
        fields = ['contact_first', 'contact_last',
                  'contact_phone', 'contact_ext', 'contact_cell', 
                  'contact_email', 'contact_notes','contact_afterhours', 'contact_site_id',
                  'contact_247_name', 'contact_247_phone', 'contact_247_email', 'contact_247_notes'
                  ]

# create site_access Form called siteAcessForm
class siteAccessForm(ModelForm):
    class Meta:
        model = site_access
        fields = ['site_access_keys', 'site_access_alarm_code', 'site_access_door_code',
                  'site_access_physical_key', 'site_access_physical_key_location', 'site_access_rack_code',
                  'site_access_gate_code', 'site_access_additional_access_notes', 'site_access_additional_access_code',
                  'site_access_notes'
                  ]

#---------------------------------------Photos---------------------------------------#   
# TODO: make photo gallery class, make it a model, add photos to it, add photos to site

# class picture(models.Model):
#     picture_name = models.CharField(max_length=100)
#     picture_body = models.TextField()
#     upload_date = models.DateTimeField(auto_now_add=True)
#     picture_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True) 
#     image = models.ImageField(upload_to=)
    
# class category(models.Model):
#     name = models.CharField(max_length=50)
        
# class reporter(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
    

    
    
### To show site name in list to display data ###
