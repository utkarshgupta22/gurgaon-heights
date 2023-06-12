from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Amenities)
admin.site.register(Image)
admin.site.register(City)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_type', 'title',  'location', 'area_min', 'area_max', 'price_min',
                     'price_max', 'psf', 'status', 'rating',  'title_overview', 'description_overview', 'slug' )
    
admin.site.register(Property, PropertyAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_number', 'email', 'message', 'city')

admin.site.register(Contact, ContactAdmin)



