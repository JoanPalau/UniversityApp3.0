from django.db import models

class Location(models.Model):

    address = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=8)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return "{} [{}] {}".format(self.address, self.city, self.country)
