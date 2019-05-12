from .comment import Comment
from .subject import Subject
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class SubjectComment(Comment):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(str(self.comment))

    def get_absolute_url(self):
        return reverse('subject', kwargs={'pk': self.subject.pk, 'pkd': self.subject.get_degree()})
