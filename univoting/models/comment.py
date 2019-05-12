from django.db import models
from datetime import date


class Comment(models.Model):
    comment = models.TextField(max_length=250, help_text='Write your opinion here')
    date = models.DateField(default=date.today)

    def __str__(self):
        return "{}...".format(self.comment[:15])
