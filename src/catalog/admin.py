from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(battery)
admin.site.register(battery_contact_list)
admin.site.register(battery_contacts)
admin.site.register(battery_tested_link)
admin.site.register(battery_contact_link)
admin.site.register(relion)
admin.site.register(contacts)
admin.site.register(generator)
admin.site.register(generator_contact_list)
admin.site.register(generator_contact_link)
admin.site.register(generator_contacts)
admin.site.register(generator_service_link)
admin.site.register(generator_tested_link)
admin.site.register(hvac)
admin.site.register(hvac_clean_link)
admin.site.register(hvac_contacts)
admin.site.register(hvac_service_link)
admin.site.register(hvac_temp_link)
admin.site.register(site)
admin.site.register(site_access)
admin.site.register(site_access_link)
admin.site.register(site_contact_link)
admin.site.register(site_distance)

