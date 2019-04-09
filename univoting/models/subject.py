from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Subject(models.Model):
    MAX_ECTS = 30
    MIN_ECTS = 1
    name = models.CharField(max_length=64, default="New Subject")
    ects = models.PositiveSmallIntegerField(validators=[MaxValueValidator(MAX_ECTS), MinValueValidator(MIN_ECTS)])
    description = models.TextField(max_length=250, default="No description added yet")
