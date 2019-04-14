from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Location(models.Model):

    address = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=8)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    lat = models.FloatField(verbose_name='Latitude', validators=[MaxValueValidator(90), MinValueValidator(-90)])
    long = models.FloatField(verbose_name='Longitude', validators=[MaxValueValidator(-180), MinValueValidator(180)])

    def __str__(self):
        return "{} [{}] {}".format(self.address, self.city, self.country)

    class Meta:
        unique_together = ('lat', 'long')
