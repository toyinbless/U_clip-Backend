from django.urls import path, include
from U_clip.models import Uclip_map
from rest_framework import serializers

class Uclip_mapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uclip_map
        fields = ['Quartier', 'Localite', 'Latitude', 'Longitude','Html', 'Path']