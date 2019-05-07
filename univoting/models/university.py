import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from django.urls import reverse
from univoting.models.location import Location


def validate_phone_number(value):
    if not re.match(r'^\+[0-9]?()[0-9](\s)(\d[0-9]{6,10})$', value):
        raise ValidationError(
            gettext_lazy('%(value) no es un telefon valid.'),
            params={'value': value}
        )


class University(models.Model):

    name = models.CharField(max_length=64)
    description = models.TextField(default='No description for now.')
    picture = models.CharField(max_length=32, default='noimage.png')
    telephone = models.CharField(validators=[validate_phone_number], max_length=12, blank=True)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{} [{}]".format(self.name, self.telephone)

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
