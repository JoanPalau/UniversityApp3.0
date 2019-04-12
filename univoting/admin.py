from django.contrib import admin
from univoting.models.degree import Degree, University
from univoting.models.course import Course
from univoting.models.subject import Subject

# Register your models here.
admin.site.register(University)
admin.site.register(Degree)
admin.site.register(Subject)
admin.site.register(Course)
