from django.db import models

# Create your models here.
class Uclip_map(models.Model):
    Quartier= models.CharField(max_length=250)
    Localite = models.CharField(max_length=250)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Html = models.CharField(max_length=250)
    Path = models.CharField(max_length=1000)
    

    def __unicode__(self):
        return self.Localite
#