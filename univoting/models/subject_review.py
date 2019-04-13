from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class SubjectReview(models.Model):
    MAX = 10
    MIN = 0

    MAX_WORK = 2
    MIN_WORK = 0

    WORK_LIST = (
        (0, 'LOW'),
        (1, 'MEDIUM'),
        (2, 'A LOT'),
    )

    mark = models.FloatField(default=MIN, validators=[MaxValueValidator(MAX), MinValueValidator(MIN)])
    difficulty = models.FloatField(default=MIN, validators=[MaxValueValidator(MAX), MinValueValidator(MIN)])
    # internal value used to compute the actual score
    work_score = models.FloatField(default=MIN, validators=[MaxValueValidator(MAX), MinValueValidator(MIN)])
    workVolume = models.PositiveSmallIntegerField(choices=WORK_LIST,
                                                  validators=[MaxValueValidator(MAX_WORK),
                                                              MinValueValidator(MIN_WORK)], default=MIN_WORK)
    amount = models.PositiveIntegerField()
    # comments = models.

    def __str__(self):
        return "{} {} {}".format(self.mark, self.difficulty, self.workVolume, self.amount)

    def get_absolute_url(self):
        return reverse('univoting:subject_detail', kwargs={'pk': self.pk})

    def increase_amount(self):
        self.amount += 1

    def set_work_volume(self):
        # will truncate the float
        self.workVolume = int(self.work_score + 0.5)

    def recalculate_score_on_insert(self, mark, difficulty, work_volume):
        # increase amount of votes
        self.increase_amount()
        # recalculate mean
        self.mark = self.mark + ((mark - self.mark) / self.amount)
        self.difficulty = self.difficulty + ((difficulty - self.difficulty) / self.amount)
        self.work_score = self.work_score + ((work_volume - self.work_score) / self.amount)
        # recalculate work volume
        self.set_work_volume()
