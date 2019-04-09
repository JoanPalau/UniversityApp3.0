import re
from django.core.exceptions import ValidationError
from django.db import models
from univoting.models.location import Location


def validate_phone_number(value):
    if not re.match(r'^\+[0-9]?()[0-9](\s)(\d[0-9]{6,10})$', value):
        raise ValidationError(
            gettext_lazy('%(value) no es un telefon valid.'),
            params={'value': value}
        )

class University(models.Model):

    name = models.CharField(max_length=64)
    telephone = models.CharField(validators=[validate_phone_number], max_length=12)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return "{} [{}]".format(self.name, self.telephone)


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
