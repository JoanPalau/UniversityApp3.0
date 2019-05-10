"""
from django import forms
from .models.university import University
from .models.location import Location
from .models.degree import Degree
from .models.subject_comment import SubjectComment


class UniversityForm(forms.ModelForm):

    class Meta:
        model = University
        fields = ('name', 'description', 'telephone')  # , 'location'


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'



class UniversityCreateForm(UniversityForm, LocationForm):
    field_order = ['name', 'description', 'telephone', 'address',
                   'zipcode', 'city', 'country']



class DegreeForm(forms.ModelForm):

    class Meta:
        model = Degree
        fields = ('title', 'ects', 'description')


class OpinionForm(forms.ModelForm):

    class Meta:
        model = SubjectComment
        fields = ('comment', 'subject')
"""
