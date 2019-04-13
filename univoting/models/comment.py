from django.db import models


class Comment(models.Model):
    comment = models.TextField(max_length=250, help_text='Write your opinion here')

    def __str__(self):
        return "{}...".format(self.comment[:15])
