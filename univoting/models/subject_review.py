from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class SubjectReview(models.Model):
    MAX = 10
    MIN = 0

    mark = models.FloatField(default=MIN, validators=[MaxValueValidator(MAX), MinValueValidator(MIN)])
    difficulty = models.FloatField(default=MIN, validators=[MaxValueValidator(MAX), MinValueValidator(MIN)])
    workVolume = models.FloatField(default=MIN, validators=[MaxValueValidator(MAX), MinValueValidator(MIN)])
    amount = models.PositiveIntegerField()
    # comments = models.

    def __str__(self):
        return "{} {} {}".format(self.mark, self.difficulty, self.workVolume, self.amount)

    def get_absolute_url(self):
        return reverse('univoting:subject_detail', kwargs={'pk': self.pk})

    def recalculate_scores_on_insert(self, score):
        pass
