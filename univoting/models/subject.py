from django.db import models
from django.urls import reverse
from univoting.models.subject_review import SubjectReview
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Subject(models.Model):
    MAX_ECTS = 30
    MIN_ECTS = 1

    name = models.CharField(max_length=64, default="New Subject")
    ects = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(MAX_ECTS), MinValueValidator(MIN_ECTS)],
        default=6)
    description = models.TextField(max_length=250, default="No description added yet")
    review = models.ForeignKey(SubjectReview, null=True, blank=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    _course = models.PositiveSmallIntegerField(null=True, blank=True)
    _degree = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return "Nom: {} ECTS: {}".format(self.name, self.ects)

    def get_absolute_url(self):
        return reverse('subject_detail', kwargs={'pk': self.pk})

    def get_course(self):
        return self._course

    def get_degree(self):
        return self._degree
