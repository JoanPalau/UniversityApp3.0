from django import forms
from .models.subject import Subject


class SubjectCreateForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('name', 'description', 'ects')
