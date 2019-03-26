import re
from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator


class University(models.Model):
    pass


class Degree(models.Model):
    title = models.CharField(max_length=64)
    ects = models.IntegerField(validators=[MaxLengthValidator(600), MinValueValidator(1)])
    description = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __init__(self, title, ects, description, university, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not isinstance(title, str) or re.match(r'^\s*$', title) or \
                not isinstance(ects, int) or not (0 < ects < 601) or \
                not isinstance(description, str) or \
                not isinstance(university, University):
            raise ValueError

        self.title = title
        self.ects = ects
        self.description = description
        self.university = university

    def __str__(self):
        return "{} [{}] {}".format(self.title, self.ects, self.description)
