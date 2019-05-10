import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from univoting.models.location import Location
from django.contrib.auth.models import User

"""
def validate_phone_number(value):
    if not re.match(r'^\+[0-9]?()[0-9](\s)(\d[0-9]{6,10})$', value):
        raise ValidationError(
            gettext_lazy('%(value) no es un telefon valid.'),
            params={'value': value}
        )
"""


class University(models.Model):

    name = models.CharField(max_length=64)
    description = models.TextField()
    picture = models.CharField(max_length=32, default='noimage.png', blank=True, null=True)
    # telephone = models.CharField(max_length=12, blank=True)  # validators=[validate_phone_number],
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # Location

    address = models.CharField(max_length=64, blank=True, null=True)
    zipcode = models.CharField(max_length=8, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    country = models.CharField(max_length=32, blank=True, null=True)
    lat = models.FloatField(verbose_name='Latitude', validators=[MaxValueValidator(90), MinValueValidator(-90)], blank=True, null=True)
    long = models.FloatField(verbose_name='Longitude', validators=[MaxValueValidator(180), MinValueValidator(-180)], blank=True, null=True)

    def __str__(self):
        return "{} City: {} Address: {}".format(self.name, self.city, self.address)

    def get_absolute_url(self):
        return reverse('university', kwargs={'pk': self.pk})

    '''
    @staticmethod
    def create(name, telephone, location):
        if not isinstance(name, str) or re.match(r'^\s*$', name) or \
                not isinstance(telephone, str) or \
                not isinstance(location, Location):
            raise ValueError
        university = University()
        university.name = name
        university.telephone = telephone
        university.location = location

        return university
    '''
