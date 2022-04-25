from django.db import models

# Create your models here.


class Region(models.Model):
    year = models.IntegerField()
    region_name = models.CharField(max_length=200)
    percent_air_pollution = models.FloatField()
    percent_water_pollution = models.FloatField()

    def __str__(self):
        return "{}-{}".format(self.year, self.region_name)
