from .comment import Comment
from .subject import Subject
from django.db import models


class SubjectComment(Comment):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(str(self.subject), str(self.comment))
