from django.contrib import admin
from .models import Uclip_map

class Uclip_mapAdmin(admin.ModelAdmin):
    list_display = ('Quartier', 'Localite', 'Latitude', 'Longitude','Html')
    search_fields= ('Quartier', 'Localite')

# Register your models here.
admin.site.register(Uclip_map, Uclip_mapAdmin)