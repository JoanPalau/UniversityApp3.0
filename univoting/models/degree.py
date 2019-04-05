import re
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy
from django.db import models


class University(models.Model):
    pass


def validate_title(value):
    if not re.match(r'^(\w ?)+$', value):
        raise ValidationError(
            gettext_lazy('%(value) no es un nom de producte.'),
            params={'value': value}
        )


class Degree(models.Model):
    MAX_VALUE = 600

    title = models.CharField(validators=[validate_title], max_length=64)
    ects = models.PositiveSmallIntegerField(validators=[MaxValueValidator(MAX_VALUE)])
    description = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return "{} [{}] {}".format(self.title, self.ects, self.description)

    @staticmethod
    def create(title, ects, description, university):
        if not isinstance(title, str) or re.match(r'^\s*$', title) or \
                not isinstance(ects, int) or not (0 < ects < 601) or \
                not isinstance(description, str) or \
                not isinstance(university, University):
            raise ValueError
        degree = Degree()
        degree.title = title
        degree.ects = ects
        degree.description = description
        degree.university = university

        return degree
