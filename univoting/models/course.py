from django.db import models
from . import degree, subject


class Course(models.Model):

    COURSE_LIST = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5, 'Fifth'),
    )

    degree_id = models.ForeignKey(degree.Degree, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subject.Subject, on_delete=models.CASCADE)
    course = models.SmallIntegerField(choices=COURSE_LIST)

    class Meta:
        ordering = ['course']
        unique_together = {'degree_id', 'subject_id'}

    def __str__(self):
        return "{} {} {}".format(self.degree_id.title, self.subject_id.name, self.course)
