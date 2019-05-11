from django import forms
from .models.subject import Subject
from .models.degree import Degree
from .models.subject_comment import SubjectComment


class SubjectCreateForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('name', 'description', 'ects')

